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
    name:'BaseBarChart',
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
            title: this.MyChartTitle,
            yaxis:{title:{text:this.yaxisTitle}},
            xaxis:{title:{text:this.xaxisTitle}},
        }
        }
    },
    props: ['barChartData','MyChartTitle','yaxisTitle','xaxisTitle']
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>