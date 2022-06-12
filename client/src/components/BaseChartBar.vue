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
    name:'BaseChartBar',
    components: {
    Plotly
    },
    data() {
        return {
        data:[{
            x: this.barChartData.Xaxis,
            y: this.barChartData.Yaxis,
            type:"bar"
        }],
        layout:{
            title: {text:this.MyChartTitle, font:{size:27}},
            yaxis:{title:{text:this.yaxisTitle}},
            xaxis:{title:{text:this.xaxisTitle}},
            width: 900,
            height: 825,
        }
        }
    },
    props: ['barChartData','MyChartTitle','yaxisTitle','xaxisTitle']
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>