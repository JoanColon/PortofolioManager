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
            id='ChartBarLine'
            v-if='!isLoading'
            :MyChartTitle='HistoricChartTitle' 
            :barChartData='HistoricChartData' 
            :yaxisTitle='Historic_yaxisTitle'
            :xaxisTitle='Historic_xaxisTitle' 
            />
          </b-col>


          <b-col>
            <h3>Profitability Information</h3>
          <!-- Table of total diviend per company -->
            <BaseTableStatic
            id="ProfitabilityTable"
            class='Table' 
            v-if='!isLoading' 
            :MyTableItems='ProfitabilityTableData' 
            :MyTableFields='ProfitabilityTableFields'
          />

          </b-col>
        </b-row>
      </b-tab>

      <!----------------------------------------------------------------------------------->
      <!--------------------------- HISTORIC DIVIDENDS TAB -------------------------------->
      <!----------------------------------------------------------------------------------->
      <b-tab title="Dividends">
        <b-row>
          <b-col>
          <!-- Chart of total dividend per year -->
            <BaseChartBar 
            v-if='!isLoading' 
            :barChartData='dividendYear' 
            :MyChartTitle='MyChartTitle'
            :yaxisTitle='yaxisTitle'
            :xaxisTitle='xaxisTitle'  
          />
          </b-col>

          <b-col>
            <h3>Total dividends received by company</h3>
          <!-- Table of total diviend per company -->
            <BaseTable
            id="DividendTable"
            class='Table'  
            v-if='!isLoading' 
            :MyTableItems='dividendCompany' 
            :MyTableFields='dividendCompanyFields'
            :RowPerPage=13
          />
          </b-col>
        </b-row>
      </b-tab>

      <!----------------------------------------------------------------------------------->
      <!--------------------------- HISTORIC BENCHMARK TAB -------------------------------->
      <!----------------------------------------------------------------------------------->
      <b-tab title="Benchmarks">
        <b-row>
          <div class="SliderRange">
            <FormBenchmarks/>
          </div>
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
import BaseChartBar from '@/components/BaseChartBar.vue'
import BaseTableStatic from '@/components/BaseTableStatic.vue' 
import BaseTable from '@/components/BaseTable.vue'
import FormBenchmarks from '@/components/FormBenchmarks.vue'


export default {
  name: 'ViewDividends',
  components: {
    BaseCard,
    BaseTable,
    BaseTableStatic,
    BaseChartBarLine,
    BaseChartBar,
    FormBenchmarks,
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
      TotalDividendsValue:'',

      // data for Yield on Cost BaseCard
      YieldOnCostImage:'Yield.png',
      YieldOnCostTitle:'Yield on Cost: ',
      YieldOnCostValue:'',

      // --------------------------- HISTORIC PORTOFOLIO DATA  ------------------------------------ //
      // data for the bar/line chart
      HistoricChartData:[],
      HistoricChartTitle:'Historic perfomance of the portofolio',
      Historic_xaxisTitle:'Year',
      Historic_yaxisTitle:'Euros (€)',

      // data for the profitability table
      ProfitabilityTableData:[],
      ProfitabilityTableFields:[
        {key:'ProfitabilityRatio', sortable: false, label:'Profitability Ratio'},
        {key:'Value', sortable: false, label:'Value'}
      ],

      // --------------------------- HISTORIC DIVIDEND DATA  ------------------------------------ //
      // data for the bar chart
      dividendYear:[], //dividends received per year
      MyChartTitle:'Dividends received per year',
      xaxisTitle:'Year',
      yaxisTitle:'Gross €/year',
    
      // data for the dividend table
      dividendCompany: [], //dividend received by company
      dividendCompanyFields:[
        {key:'MyTicker', sortable: true, label:'Ticker' },
        {key:'AmountEuro', sortable: true, label:'Amount (€)' },
      ],

      // --------------------------- BENCHMARK DATA ----------------------------------------------- //

      // all benchmark data and layout is found int he the FormBenchmarks.vue


      //to prevent that the chart and the table are rendered before receiving the data
      isLoading: false, 
    };
  },
  methods:{
    // call to flask to get historic portofolio data
    async getHistoricData(){
      try{
        this.isLoading = true
        
        const path = 'http://localhost:5000/historicInformation'; //path to flask route
        let {data} = await axios.get(path)

        // Portofolio data = data[0] from axios call
        this.HistoricChartData=data[0]
        this.AddedFundsValue=data[0][4]

        // Dividned data = data[1] from axios call
        this.dividendCompany = data[1][0]; //dividendCompany is the variable (empty list) defined in data() section, gets dividend received per company
        this.dividendYear = data[1][1] //dividendYear is the variable (empty list) defined in data() section, gets dividend received per year
        this.TotalDividendsValue = data[1][2]

        // Yield on Cost data = data[2] from axios call
        this.YieldOnCostValue = data[2]

        // Profitability data = data[3] from axios call
        this.ProfitabilityTableData=[
          {'ProfitabilityRatio':'Total Return (€)', 'Value': data[3][0]},
          {'ProfitabilityRatio':'Total Return (%)', 'Value': data[3][1]},
          {'ProfitabilityRatio':'Time Weighted Return', 'Value': data[3][2]},
          {'ProfitabilityRatio':'Time Weighted Rate of Return', 'Value': data[3][3]},
          {'ProfitabilityRatio':'Money Weighted Rate of Return', 'Value': data[3][4]},
        ]

        this.isLoading = false
      } catch(error){console.error(error)}
    },
  },
  mounted(){
    this.getHistoricData(); //calls the function getHistoricPortofolioData when mounting the view
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

.Table{
  width:75%;
  margin-left:auto;
  margin-right: auto;
}

#ChartBarLine{
  margin-top:0px;
}

.ProfitabilityDiv{
  margin-top:75px;
  margin-left:100px;
  }

h3{
  margin-top:25px;
  margin-bottom:25px;
  text-align: center;
}

</style>