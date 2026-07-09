import plotly.express as px

# Load data
data = px.data.gapminder()

fig = px.scatter(
    data,
    x="gdpPercap",
    y="lifeExp",
    animation_frame="year",
    animation_group="country",
    size="pop",
    color="continent",
    hover_name="country",

    # Extra information in hover
    hover_data={
        "gdpPercap":":,.0f",
        "lifeExp":":.1f",
        "pop":":,",
        "continent":True
    },

    log_x=True,
    size_max=60,

    range_x=[100,100000],
    range_y=[25,90],

    title="🌍 Gapminder Data Visualization",

    labels={
        "gdpPercap":"GDP per Capita ($)",
        "lifeExp":"Life Expectancy (Years)"
    },

    template="plotly_dark",
    color_discrete_sequence=px.colors.qualitative.Plotly,
)

# Bubble style
fig.update_traces(
    marker=dict(
        opacity=0.8,
        line=dict(
            width=1,
            color="white"
        )
    )
)

# Layout
fig.update_layout(

    title=dict(
        text="🌍 Gapminder Data Visualization",
        x=0.5,
        xanchor="center",
        font=dict(size=28)
    ),

    font=dict(size=15),

    xaxis_title_font=dict(size=18),
    yaxis_title_font=dict(size=18),

    legend_title_text="Continent",

    width=1200,
    height=700,

    margin=dict(l=60,r=60,t=80,b=60),

    hoverlabel=dict(
        bgcolor="black",
        font_size=14,
        font_family="Arial"
    ),

    transition=dict(
        duration=500
    )
)

# Grid style
fig.update_xaxes(
    title_standoff=25,
    showgrid=True,
    gridcolor="rgba(255,255,255,0.15)"
)

fig.update_yaxes(
    title_standoff=25,
    showgrid=True,
    gridcolor="rgba(255,255,255,0.15)"
)

fig.show()

fig.write_html(
    "animated_scatter_plot.html",
    include_plotlyjs="cdn"
)