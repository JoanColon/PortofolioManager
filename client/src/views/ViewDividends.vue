<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
  <div class="dividends">
      <h3 class="m-4">Total dividends received: {{totalReceivedDividends}} €</h3>
      <b-row>
        <b-col>
        <!-- Chart of total dividend per year -->
          <BaseBarChart 
          v-if='!isLoading' 
          :barChartData='dividendYear' 
          :MyChartTitle='MyChartTitle'
          :yaxisTitle='yaxisTitle'
          :xaxisTitle='xaxisTitle'  
        />
        </b-col>
        <b-col>
        <!-- Table of total diviend per company -->
          <BaseTable
          id="DividendTable" 
          v-if='!isLoading' 
          :MyTableItems='dividendCompany' 
          :MyTableFields='dividendCompanyFields'
          :RowPerPage='RowsPerPage' 
        />
        </b-col>
      </b-row>
  </div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
import axios from 'axios';

// import components
import BaseBarChart from '@/components/BaseBarChart.vue' //@ redirects to src folder
import BaseTable from '@/components/BaseTable.vue' 

export default {
  name: 'ViewDividends',
  components: {
    BaseBarChart,
    BaseTable
  },
  data(){
    return{
      // data for total received dividends 
      totalReceivedDividends:'',

      // data for the bar chart
      dividendYear:[], //dividends received per year
      MyChartTitle:'Dividends received per year',
      xaxisTitle:'',
      yaxisTitle:'Gross €/year',
    
      // data for the dividend table
      dividendCompany: [], //dividend received by company
      dividendCompanyFields:[
        {key:'Tickers', sortable: true },
        {key:'Amount_euro', sortable: true, label:'Amount (€)' },
        ],
      RowsPerPage:10,

      //to prevent that the chart and the table are rendered before receiving the data
      isLoading: false, 
    };
  },
  methods:{
    //call to flack to get dividend data (per year and per company) 
    getPortofolioDividendData(){
      this.isLoading = true
      const path = 'http://localhost:5000/historicDividends'; //path to flask route  
      axios.get(path)
        .then((res) => {
          this.dividendCompany = res.data[0]; //dividendCompany is the variable (empty list) defined in data() section, gets dividend received per company
          this.dividendYear = res.data[1] //dividendYear is the variable (empty list) defined in data() section, gets dividend received per year
          this.isLoading = false
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  mounted(){
    this.getPortofolioDividendData(); //calls the function getPortofolioData when mounting the view
  },
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>
#DividendTable{
    width:75%;
    margin-left:auto;
    margin-right: auto;
}
</style>