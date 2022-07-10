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
    name:'BaseChartLineMultiple',
    components: {
    Plotly
    },
    data() {
        return {
            data: this.lineChartData,
            layout:{
                title: {text:this.MyChartTitle, font:{size:27}},
                yaxis:{title:{text:this.yaxisTitle}},
                xaxis:{
                    title:{text:this.xaxisTitle},
                    tickformat:'d'
                },
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