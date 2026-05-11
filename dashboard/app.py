import dash
from dash import dcc, html, Input, Output, dash_table
import plotly.express as px
import pandas as pd
import os

# Load the data - FIXED PATH for deployment
df = pd.read_csv('customer_data.csv')

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server  # This is required for deployment

app.layout = html.Div([
    html.H1("🎯 Customer Segmentation Dashboard", style={'textAlign': 'center'}),
    html.H4("RFM Analysis | Customer Segments | Business Insights", style={'textAlign': 'center'}),
    html.Hr(),
    
    # Filters
    html.Div([
        html.Div([
            html.Label("Select Segment:"),
            dcc.Dropdown(
                id='segment-dropdown',
                options=[{'label': 'All', 'value': 'All'}] + 
                        [{'label': s, 'value': s} for s in df['Segment'].unique()],
                value='All'
            )
        ], style={'width': '30%', 'display': 'inline-block'}),
        
        html.Div([
            html.Label("Min Monetary Value ($):"),
            dcc.Slider(id='monetary-slider', min=0, max=df['Monetary'].max(), value=0,
                      marks={0: '$0', int(df['Monetary'].max()/2): f'${int(df["Monetary"].max()/2)}', 
                             int(df['Monetary'].max()): f'${int(df["Monetary"].max())}'})
        ], style={'width': '60%', 'display': 'inline-block', 'marginLeft': '20px'})
    ]),
    
    html.Button("Download Data", id="download-btn", n_clicks=0),
    dcc.Download(id="download-data"),
    
    html.Hr(),
    
    # KPI Row
    html.Div([
        html.Div([html.H3("Total Customers"), html.H2(id="total-customers")], 
                style={'width': '23%', 'display': 'inline-block', 'backgroundColor': '#f0f0f0', 
                       'padding': '10px', 'borderRadius': '10px', 'textAlign': 'center'}),
        html.Div([html.H3("Total Revenue"), html.H2(id="total-revenue")], 
                style={'width': '23%', 'display': 'inline-block', 'backgroundColor': '#f0f0f0', 
                       'padding': '10px', 'borderRadius': '10px', 'textAlign': 'center'}),
        html.Div([html.H3("Avg Order Value"), html.H2(id="avg-order")], 
                style={'width': '23%', 'display': 'inline-block', 'backgroundColor': '#f0f0f0', 
                       'padding': '10px', 'borderRadius': '10px', 'textAlign': 'center'}),
        html.Div([html.H3("Avg Recency"), html.H2(id="avg-recency")], 
                style={'width': '23%', 'display': 'inline-block', 'backgroundColor': '#f0f0f0', 
                       'padding': '10px', 'borderRadius': '10px', 'textAlign': 'center'})
    ]),
    
    html.Hr(),
    
    # Charts
    html.Div([
        dcc.Graph(id="scatter-plot", style={'width': '49%', 'display': 'inline-block'}),
        dcc.Graph(id="pie-chart", style={'width': '49%', 'display': 'inline-block'})
    ]),
    
    html.Div([
        dcc.Graph(id="monetary-chart", style={'width': '32%', 'display': 'inline-block'}),
        dcc.Graph(id="frequency-chart", style={'width': '32%', 'display': 'inline-block'}),
        dcc.Graph(id="recency-chart", style={'width': '32%', 'display': 'inline-block'})
    ]),
    
    html.Hr(),
    
    # Recommendations
    html.Div([
        html.H3("💡 Business Recommendations"),
        html.Div(id="recommendations", style={'backgroundColor': '#e8f4f8', 'padding': '15px', 'borderRadius': '10px'})
    ]),
    
    html.Hr(),
    
    # Data Table
    html.H3("📋 Customer Data"),
    dash_table.DataTable(id="data-table", page_size=10, 
                        style_table={'overflowX': 'scroll'},
                        style_cell={'textAlign': 'left'})
])

# Callbacks
@app.callback(
    [Output("total-customers", "children"),
     Output("total-revenue", "children"),
     Output("avg-order", "children"),
     Output("avg-recency", "children"),
     Output("scatter-plot", "figure"),
     Output("pie-chart", "figure"),
     Output("monetary-chart", "figure"),
     Output("frequency-chart", "figure"),
     Output("recency-chart", "figure"),
     Output("recommendations", "children"),
     Output("data-table", "data"),
     Output("data-table", "columns")],
    [Input("segment-dropdown", "value"),
     Input("monetary-slider", "value")]
)

def update_dashboard(segment, min_monetary):
    filtered = df.copy()
    if segment != 'All':
        filtered = filtered[filtered['Segment'] == segment]
    filtered = filtered[filtered['Monetary'] >= min_monetary]
    
    total_customers = f"{len(filtered):,}"
    total_revenue = f"${filtered['Monetary'].sum():,.0f}"
    avg_order = f"${filtered['Monetary'].mean():,.0f}"
    avg_recency = f"{filtered['Recency'].mean():.0f} days"
    
    scatter = px.scatter(filtered, x='Recency', y='Monetary', color='Segment',
                         title='Recency vs Monetary Value', 
                         hover_data=['CustomerID', 'Frequency'],
                         size='Frequency', size_max=20)
    
    pie = px.pie(filtered, names='Segment', title='Segment Distribution')
    
    monetary_chart = px.bar(filtered.groupby('Segment')['Monetary'].mean().reset_index(),
                           x='Segment', y='Monetary', title='Avg Monetary by Segment', 
                           color='Segment', text_auto='.0f')
    
    frequency_chart = px.bar(filtered.groupby('Segment')['Frequency'].mean().reset_index(),
                            x='Segment', y='Frequency', title='Avg Frequency by Segment', 
                            color='Segment', text_auto='.1f')
    
    recency_chart = px.bar(filtered.groupby('Segment')['Recency'].mean().reset_index(),
                          x='Segment', y='Recency', title='Avg Recency by Segment', 
                          color='Segment', text_auto='.0f')
    
    if segment == 'All':
        recommendations = html.Div([
            html.Ul([
                html.Li("🔴 VIP Customers: Send loyalty rewards, premium offers, early access"),
                html.Li("🟠 Loyal Customers: Referral program, cross-sell products"),
                html.Li("🟡 At-Risk Customers: Re-engagement emails, win-back discounts"),
                html.Li("🟢 New Customers: Welcome series, onboarding education")
            ])
        ])
    elif segment == 'VIP':
        recommendations = html.Div([
            html.Ul([
                html.Li("✓ Send exclusive loyalty rewards and early access"),
                html.Li("✓ Offer premium membership with free shipping"),
                html.Li("✓ Personal thank you notes and birthday gifts")
            ])
        ])
    elif segment == 'Loyal':
        recommendations = html.Div([
            html.Ul([
                html.Li("✓ Implement referral program (give $20, get $20)"),
                html.Li("✓ Cross-sell complementary products"),
                html.Li("✓ Offer loyalty points that never expire")
            ])
        ])
    elif segment == 'At-Risk':
        recommendations = html.Div([
            html.Ul([
                html.Li("✓ Send re-engagement emails with 20-30% discount"),
                html.Li("✓ Offer win-back campaigns: 'We miss you'"),
                html.Li("✓ Send customer satisfaction survey")
            ])
        ])
    elif segment == 'New':
        recommendations = html.Div([
            html.Ul([
                html.Li("✓ Welcome series emails with onboarding education"),
                html.Li("✓ First-purchase discount for next order (15%)"),
                html.Li("✓ Product tutorials and usage guides")
            ])
        ])
    else:
        recommendations = html.Div([
            html.Ul([
                html.Li("✓ Nurture with consistent email communication"),
                html.Li("✓ Offer bundle deals to increase order value")
            ])
        ])
    
    columns = [{"name": i, "id": i} for i in filtered[['CustomerID', 'Segment', 'Recency', 'Frequency', 'Monetary', 'RFM_Numeric']].columns]
    data = filtered[['CustomerID', 'Segment', 'Recency', 'Frequency', 'Monetary', 'RFM_Numeric']].to_dict('records')
    
    return total_customers, total_revenue, avg_order, avg_recency, scatter, pie, monetary_chart, frequency_chart, recency_chart, recommendations, data, columns

@app.callback(
    Output("download-data", "data"),
    Input("download-btn", "n_clicks"),
    prevent_initial_call=True
)
def download_data(n_clicks):
    return dcc.send_data_frame(df.to_csv, "customer_segments_export.csv")

if __name__ == '__main__':
    app.run(debug=True)