from dash import Dash, html, dcc, callback, Output, Input

# 创建 Dash 应用
app = Dash(__name__)
server = app.server
# 设置应用布局
app.layout = html.Div(style={'display': 'flex', 'height': '100vh'}, children=[
    # 左侧导航栏
    html.Div(style={'width': '200px', 'backgroundColor': '#f8f9fa', 'padding': '10px'}, children=[
        html.H2("导航", style={'textAlign': 'center'}),
        dcc.Link("首页", href='/', style={'display': 'block', 'margin': '10px 0'}),
        dcc.Link("页面 1", href='/page-1', style={'display': 'block', 'margin': '10px 0'}),
        dcc.Link("页面 2", href='/page-2', style={'display': 'block', 'margin': '10px 0'}),
    ]),
    
    # 右侧内容区域
    html.Div(style={'flex': '1', 'padding': '20px'}, children=[
        html.H1("欢迎使用 Dash 应用", style={'textAlign': 'center'}),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])
])

# 页面内容回调
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return html.Div([
            html.H3("首页内容"),
            html.P("这是首页的内容。")
        ])
    elif pathname == '/page-1':
        return html.Div([
            html.H3("页面 1 内容"),
            html.P("这是页面 1 的内容。")
        ])
    elif pathname == '/page-2':
        return html.Div([
            html.H3("页面 2 内容"),
            html.P("这是页面 2 的内容。")
        ])
    else:
        return html.Div([
            html.H3("404 页面未找到"),
            html.P("您访问的页面不存在。")
        ])
    
if __name__ == '__main__':
    app.run(host="0.0.0.0",port="8000",debug=True)