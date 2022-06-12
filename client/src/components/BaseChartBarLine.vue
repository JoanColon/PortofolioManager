<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
    <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
import { Plotly } from 'vue-plotly'

export default {
    name:'BaseChartBarLine',
    components: {
    Plotly
    },
    data() {
        return {
        data:[
            {
                x: this.barChartData[0],
                y: this.barChartData[1],
                name: 'Yearly added Funds',
                type:"bar"
            },
            {
                x: this.barChartData[0],
                y: this.barChartData[2],
                name: 'Total added funds',
                type:"scatter"
            },
            {
                x: this.barChartData[0],
                y: this.barChartData[3],
                name: 'Portofolio value',
                type:"scatter"
            },
        ],
        layout:{
            title: {text:this.MyChartTitle, font:{size:27}},
            yaxis:{title:{text:this.yaxisTitle}},
            xaxis:{title:{text:this.xaxisTitle}},
            showlegend: true,
            legend: {"orientation": "h", x:0.25},
            width: 1000,
            height: 800,
        },
        }
    },
    props: ['barChartData','MyChartTitle','yaxisTitle','xaxisTitle']
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>