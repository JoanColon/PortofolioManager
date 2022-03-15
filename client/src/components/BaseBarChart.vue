<template>
<div>
    <Plotly :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
</div>
</template>

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
            title: "My title"
        }
        }
    },
    props: ['barChartData']
}
</script>
