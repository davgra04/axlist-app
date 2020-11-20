from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

import datetime as dt

from axlist.db import get_db

bp = Blueprint("accesslist", __name__)


@bp.route("/")
def index():
    # get data from db
    db = get_db()
    axlist = db.execute(
        "SELECT ts, ip, method, path FROM accesslist ORDER BY id DESC LIMIT 500"
    ).fetchall()

    # figure out timezone
    # I don't know what is going on here.... surely there's a better way
    tzname = dt.datetime.now().astimezone().tzinfo.tzname(dt.datetime.now())

    # form data and render
    data = {
        "axlist": list(axlist),
        "tzname": tzname,
    }

    return render_template("accesslist.html", data=data)


@bp.route("/debug")
def debug():

    debug = {
        "request": {
            "request.environ": request.environ,
            "request.path": request.path,
            "request.full_path": request.full_path,
            "request.script_root": request.script_root,
            "request.url": request.url,
            "request.base_url": request.base_url,
            "request.url_root": request.url_root,
            "request.accept_charsets": request.accept_charsets,
            "request.accept_encodings": request.accept_encodings,
            "request.accept_languages": request.accept_languages,
            "request.accept_mimetypes": request.accept_mimetypes,
            "request.access_control_request_headers": request.access_control_request_headers,
            "request.access_control_request_method": request.access_control_request_method,
            "request.access_route": request.access_route,
            "request.args": request.args,
            "request.authorization": request.authorization,
            "request.base_url": request.base_url,
            "request.blueprint": request.blueprint,
            "request.cache_control": request.cache_control,
            "request.close": request.close,
            "request.content_encoding": request.content_encoding,
            "request.content_length": request.content_length,
            "request.content_md5": request.content_md5,
            "request.content_type": request.content_type,
            "request.cookies": request.cookies,
            "request.data": request.data,
            "request.date": request.date,
            "request.dict_storage_class": request.dict_storage_class,
            "request.endpoint": request.endpoint,
            "request.files": request.files,
            "request.form": request.form,
            "request.form_data_parser_class": request.form_data_parser_class,
            "request.full_path": request.full_path,
            "request.get_data": request.get_data,
            "request.get_json": request.get_json,
            "request.headers": request.headers,
            "request.host": request.host,
            "request.host_url": request.host_url,
            "request.if_match": request.if_match,
            "request.if_modified_since": request.if_modified_since,
            "request.if_none_match": request.if_none_match,
            "request.if_range": request.if_range,
            "request.if_unmodified_since": request.if_unmodified_since,
            "request.is_json": request.is_json,
            "request.is_multiprocess": request.is_multiprocess,
            "request.is_multithread": request.is_multithread,
            "request.is_run_once": request.is_run_once,
            "request.is_secure": request.is_secure,
            "request.json": request.json,
            "request.json_module": request.json_module,
            "request.list_storage_class": request.list_storage_class,
            "request.make_form_data_parser": request.make_form_data_parser,
            "request.max_content_length": request.max_content_length,
            "request.max_forwards": request.max_forwards,
            "request.method": request.method,
            "request.mimetype": request.mimetype,
            "request.mimetype_params": request.mimetype_params,
            "request.on_json_loading_failed": request.on_json_loading_failed,
            "request.origin": request.origin,
            "request.parameter_storage_class": request.parameter_storage_class,
            "request.path": request.path,
            "request.pragma": request.pragma,
            "request.query_string": request.query_string,
            "request.range": request.range,
            "request.referrer": request.referrer,
            "request.remote_addr": request.remote_addr,
            "request.remote_user": request.remote_user,
            "request.routing_exception": request.routing_exception,
            "request.scheme": request.scheme,
            "request.script_root": request.script_root,
            "request.stream": request.stream,
            "request.url": request.url,
            "request.url_charset": request.url_charset,
            "request.url_root": request.url_root,
            "request.url_rule": request.url_rule,
            "request.user_agent": request.user_agent,
            "request.values": request.values,
            "request.view_args": request.view_args,
            "request.want_form_data_parsed": request.want_form_data_parsed,
        }
    }

    return render_template("debug.html", debug=debug)

