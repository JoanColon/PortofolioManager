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
    name:'BaseChartLine',
    components: {
    Plotly
    },
    data() {
        return {
        data:[{
            x: this.lineChartData[0],
            y: this.lineChartData[1],
            type:"scatter"
        }],
        layout:{
            title: {text:this.MyChartTitle, font:{size:27}},
            yaxis:{title:{text:this.yaxisTitle}},
            xaxis:{title:{text:this.xaxisTitle}},
            width: 900,
            height: 700,
        }
        }
    },
    props: ['lineChartData','MyChartTitle','yaxisTitle','xaxisTitle']
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>