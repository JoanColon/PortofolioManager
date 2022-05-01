<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
    <Plotly :data="data" :layout="layout"></Plotly>
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
import { Plotly } from 'vue-plotly'

export default {
    name:'BaseChartPie',
    components: {
    Plotly
    },
    data() {
        return {
        data:[{
            type: 'pie',
            values: this.pieChartData,
            labels: this.pieChartLabels,
            textinfo: "label+percent",
        }],
        layout:{
            title: this.MyChartTitle,
            showlegend: false,
            height: 800,
            width: 800,
        }
        }
    },
    props: ['pieChartData','pieChartLabels','MyChartTitle']
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>