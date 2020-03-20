from app import get_logger, get_config
import math
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import utils
from app.models import CfgNotify
from app.admin.forms import CfgNotifyForm
from . import admin
from . import mychart
import os

logger = get_logger(__name__)
cfg = get_config()

# 通用列表查询
def common_list(DynamicModel, view):
    # 接收参数
    action = request.args.get('action')
    id = request.args.get('id')
    page = int(request.args.get('page')) if request.args.get('page') else 1
    length = int(request.args.get('length')) if request.args.get('length') else cfg.ITEMS_PER_PAGE

    # 删除操作
    if action == 'del' and id:
        try:
            DynamicModel.get(DynamicModel.id == id).delete_instance()
            flash('删除成功')
        except:
            flash('删除失败')

    # 查询列表
    query = DynamicModel.select()
    total_count = query.count()

    # 处理分页
    if page: query = query.paginate(page, length)

    dict = {'content': utils.query_to_list(query), 'total_count': total_count,
            'total_page': math.ceil(total_count / length), 'page': page, 'length': length}
    return render_template(view, form=dict, current_user=current_user)


# 通用单模型查询&新增&修改
def common_edit(DynamicModel, form, view):
    id = request.args.get('id', '')
    if id:
        # 查询
        model = DynamicModel.get(DynamicModel.id == id)
        if request.method == 'GET':
            utils.model_to_form(model, form)
        # 修改
        if request.method == 'POST':
            if form.validate_on_submit():
                utils.form_to_model(form, model)
                model.save()
                flash('修改成功')
            else:
                utils.flash_errors(form)
    else:
        # 新增
        if form.validate_on_submit():
            model = DynamicModel()
            utils.form_to_model(form, model)
            model.save()
            flash('保存成功')
        else:
            utils.flash_errors(form)
    return render_template(view, form=form, current_user=current_user)


# 根目录跳转
@admin.route('/', methods=['GET'])
@login_required
def root():
    return redirect(url_for('main.index'))


# 首页
@admin.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('admin/index.html', current_user=current_user)


# 通知方式查询
@admin.route('/notifylist', methods=['GET', 'POST'])
@login_required
def notifylist():
    return common_list(CfgNotify, 'admin/notifylist.html')


# 通知方式配置
@admin.route('/notifyedit', methods=['GET', 'POST'])
@login_required
def notifyedit():
    return common_edit(CfgNotify, CfgNotifyForm(), 'admin/notifyedit.html')


@admin.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'GET':
        return render_template('admin/new_drop.html')
    elif request.method == 'POST':
        file = request.files['file']
        file.save("app/upload_data/xxx.tmp")
        print(os.getcwd())
        return redirect(url_for('admin.index'))
    else:
        return render_template('errors/404.html')

# For Test
@admin.route('/charts')
@login_required
def charts():
    REMOTE_HOST="https://pyecharts.github.io/assets/js"
    liquid = mychart.liquid.render_embed()
    parallel = mychart.parallel.render_embed()
    heatmap = mychart.heatmap.render_embed()

    return render_template('admin/charts.html',
    pie_chart=liquid,
    lines_chart=parallel,
    table_chart=heatmap,
    host=REMOTE_HOST)
