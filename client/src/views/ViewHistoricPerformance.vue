<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div class="ViewGeneralLayout">
  <b-row>
    <!----------------------------------------------------------------------------------->
    <!---------------------------- FIXED CARDS ------------------------------------------>
    <!----------------------------------------------------------------------------------->
    <!------- Cards showing current funds added, total dividends and yield ib cist ------>
    <div class="BaseCards">
      <BaseCard
        :imageName='AddedFundsImage'
        :title='AddedFundsTitle'
        :data='AddedFundsValue'
      />

      <BaseCard
        :imageName='TotalDividendsImage'
        :title='TotalDividendsTitle'
        :data='TotalDividendsValue'
      />

      <BaseCard
        :imageName='YieldOnCostImage'
        :title='YieldOnCostTitle'
        :data='YieldOnCostValue'
      />
    </div>
  </b-row>

  <b-row>
    <b-tabs content-class="mt-3">
      <!----------------------------------------------------------------------------------->
      <!-------------------------- HISTORIC PORTOFOLIO TAB -------------------------------->
      <!----------------------------------------------------------------------------------->
      <b-tab title="Portofolio">
        <b-row>
          <b-col>
            <BaseChartBarLine
            v-if='!isLoading' 
            :barChartData='HistoricChartData' 
            :MyChartTitle='HistoricChartTitle'
            :yaxisTitle='Historic_yaxisTitle'
            :xaxisTitle='Historic_xaxisTitle' 
            />
          </b-col>

          <b-col>

          </b-col>
        </b-row>
      </b-tab>

      <!----------------------------------------------------------------------------------->
      <!--------------------------- HISTORIC DIVIDENDS TAB -------------------------------->
      <!----------------------------------------------------------------------------------->
      <b-tab title="Dividends" @click="getPortofolioDividendData()">
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
            :RowPerPage=10
          />
          </b-col>
        </b-row>
      </b-tab>
    </b-tabs>
  </b-row>
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
// imported libraries
import axios from 'axios';

// import components
import BaseCard from '@/components/BaseCard.vue' //@ redirects to src folder
import BaseChartBarLine from '@/components/BaseChartBarLine.vue'
import BaseBarChart from '@/components/BaseBarChart.vue' 
import BaseTable from '@/components/BaseTable.vue'


export default {
  name: 'ViewDividends',
  components: {
    BaseCard,
    BaseChartBarLine,
    BaseBarChart,
    BaseTable,
  },
  data(){
    return{
      // -------------------------------- CARDS DATA  ------------------------------------------- //
      // data for funds added BaseCard
      AddedFundsImage:'Portofolio.png',
      AddedFundsTitle:'Total funds added: ',
      AddedFundsValue:'',

      // data for total dividends receied BaseCard
      TotalDividendsImage:'Dividends.png',
      TotalDividendsTitle:'Total dividends received: ',
      TotalDividendsValue:'35000',

      // data for Yield on Cost BaseCard
      YieldOnCostImage:'Yield.png',
      YieldOnCostTitle:'Yield on Cost: ',
      YieldOnCostValue:'5.5%',

      // --------------------------- HISTORIC PORTOFOLIO DATA  ------------------------------------ //
      // data for the bar/line chart
      HistoricChartData:[],
      HistoricChartTitle:'Historic perfomance of the portofolio',
      Historic_xaxisTitle:'year',
      Historic_yaxisTitle:'€',

      // --------------------------- HISTORIC DIVIDEND DATA  ------------------------------------ //
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

      //to prevent that the chart and the table are rendered before receiving the data
      isLoading: false, 
    };
  },
  methods:{
    // call to flask to get historic portofolio data
    async getHistoricPortofolioData(){
      try{
        this.isLoading = true
        const path = 'http://localhost:5000/historicPortofolio'; //path to flask route
        let {data} = await axios.get(path)
        this.HistoricChartData=data
        this.AddedFundsValue=data[4]
        this.isLoading = false
      } catch(error){console.error(error)}
    },

    //call to flack to get dividend data (per year and per company) 
    async getPortofolioDividendData(){
      try{
        this.isLoading = true
        const path = 'http://localhost:5000/historicDividends'; //path to flask route
        let {data} = await axios.get(path)
        this.dividendCompany = data[0]; //dividendCompany is the variable (empty list) defined in data() section, gets dividend received per company
        this.dividendYear = data[1] //dividendYear is the variable (empty list) defined in data() section, gets dividend received per year
        this.isLoading = false  
      } catch(error){console.error(error)}
    }
  },
  mounted(){
    this.getHistoricPortofolioData(); //calls the function getHistoricPortofolioData when mounting the view
  },
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>
.ViewGeneralLayout{
  margin-top:15px;
  margin-left: 20px;
}

.BaseCards{
  display:flex;
}

#DividendTable{
    width:75%;
    margin-left:auto;
    margin-right: auto;
}
</style>