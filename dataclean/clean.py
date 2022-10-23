#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import click
import pandas as pd
from glob import glob
from pathlib import PurePath
from functools import partial

from lib import data_clean_funcs, SOUR_DIR, DEST_DIR, keywords, contain_keywords

@click.group()
def clean():
    """主命令入口."""
    pass

@clean.command()
def list():
    """列举所有数据."""
    for data_name in glob(os.path.join(SOUR_DIR, "*")):
        click.echo(PurePath(data_name).stem)

@clean.command()
@click.option('--output-format', default='xlsx', help='输出格式')
@click.argument('data_stem')
def one(output_format: str, data_stem: str):
    """清洗单个数据文件."""
    # 数据读取
    click.echo("数据读取")
    df = read_data(data_stem)

    # 通用处理
    click.echo("通用处理")
    df = common_prcess(df)

    # 差异处理
    click.echo("差异处理")
    clean_func = data_clean_funcs.get(data_stem, lambda x: x)
    df = clean_func(df)

    # 数据导出
    click.echo("数据导出")
    export_data(df, data_stem=data_stem, mode=output_format)

@clean.command()
@click.option('--output-format', default='xlsx', help='输出格式')
@click.pass_context
def all(ctx, output_format):
    """清洗所有数据."""
    for data_name in glob(os.path.join(SOUR_DIR, "*")):
        data_stem = PurePath(data_name).stem
        click.echo(f"清洗数据: {data_stem}")
        ctx.invoke(one, output_format=output_format, data_stem=data_stem)
        click.echo('-'*89)


################
#  help funcs  #
################

def read_data(data_stem: str):
    """读取数据."""

    data_path = ''
    for data_name in glob(os.path.join(SOUR_DIR, "*")):
        if data_stem in data_name:
            data_path = PurePath(data_name)

    if not data_path:
        click.echo("文件不存在.")
        sys.exit(-1)

    if data_path.suffix == ".csv":
        read_method = pd.read_csv
    elif data_path.suffix == ".xlsx":
        read_method = pd.read_excel

    df = read_method(data_path)

    return df

def export_data(df, data_stem:str, mode: str):
    """导出数据"""
    if mode == 'xlsx':
        try:
            output_path = os.path.join(DEST_DIR, ".".join([data_stem, mode]))
            df.to_excel(output_path, index=False)
        except:
            click.echo("导出为xlsx失败,尝试导出为csv")
            mode = 'csv'
    if mode == 'csv':
        output_path = os.path.join(DEST_DIR, ".".join([data_stem, mode]))
        df.to_csv(output_path, index=False)
    click.echo(f"数据导出到: {output_path}")


def common_prcess(df: pd.DataFrame):
    """通用数据清洗逻辑."""
    # 类型转换
    df = df.convert_dtypes()
    df['content'] = df['content'].astype('str')

    # 筛选包含关键字的观测
    df = df[df['content'].map(partial(contain_keywords, keywords=keywords))]

    # 去除换行
    df['content'] = df['content'].str.replace('\n', '')
    return df


if __name__ == "__main__":
    clean()

