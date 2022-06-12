<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>

  <!------------------------ GENERAL FORMS-------------------------------->
  <h3>General Forms</h3>
  <div class="FormGroup" id="GeneralForms">
    <!-- New Company -->
    <BaseCardDataManag
      :imageName='ImageNewCompany'
      :title='TitleNewCompany'
      v-b-modal.modalNewCompany
    />

    <b-modal id="modalNewCompany" hide-footer title="Add a new Company">
      <FormNewCompany/>
    </b-modal>

    <!-- New Order -->
    <BaseCardDataManag
      :imageName='ImageNewOrder'
      :title='TitleNewOrder'
      v-b-modal.modalNewOrder
    />

    <b-modal id="modalNewOrder" hide-footer title="Add a new Order">
      <FormNewOrder/>
    </b-modal>

    <!-- Update Dividend -->
    <BaseCardDataManag
      :imageName='ImageUpdateDividend'
      :title='TitleUpdateDividend'
      v-b-modal.modalUpdateDividend
    />

    <b-modal id="modalUpdateDividend" hide-footer title="Update Dividend">

    </b-modal>
  </div>

  <!------------------------ PORTOFOLIO FORMS-------------------------------->
  <hr>
  <h3>Portofolio Forms</h3>
  <div class="FormGroup" id="GeneralForms">
    <!-- Update Portofolio -->
    <BaseCardDataManag
      :imageName='ImagePortofolioUpdate'
      :title='TitlePortofolioUpdate'
      v-b-modal.modalPortofolioUpdate
    />

    <b-modal id="modalPortofolioUpdate" hide-footer title="Update Portofolio">
        <FormUpdatePortofolio/>
    </b-modal>

  </div>

  <!------------------------ HISTORIC PERFORMANCE FORMS-------------------------------->
  <hr>
  <h3>Historic Performance Forms</h3>
  <div class="FormGroup" id="GeneralForms">
    <!-- Import Anual NAV -->
    <BaseCardDataManag
      :imageName='ImageUpdateAnnualNAV'
      :title='TitleUpdateAnnualNAV'
      v-b-modal.modalUpdateAnnualNAV
    />

    <b-modal id="modalUpdateAnnualNAV" hide-footer title="Update Annual NAV">

    </b-modal>    

    <!-- Import Anual dividends -->
    <BaseCardDataManag
      :imageName='ImageImportAnnualDividends'
      :title='TitleImportAnnualDividends'
      v-b-modal.modalImportAnnualDividends
    />

    <b-modal id="modalImportAnnualDividends" hide-footer title="Import Anual Dividends">
      <FormImportAnualDividends/>
    </b-modal>

  </div>
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
// import components
import FormNewCompany from '@/components/FormNewCompany.vue' //@ redirects to src folder
import FormNewOrder from '@/components/FormNewOrder.vue'
import FormImportAnualDividends from '@/components/FormImportAnualDividends.vue'
import FormUpdatePortofolio from '@/components/FormUpdatePortofolio.vue'
import BaseCardDataManag from '@/components/BaseCardDataManag.vue'

export default {
  name: 'ViewDataManagement',
  components: {
    BaseCardDataManag,
    FormNewCompany,
    FormNewOrder,
    FormImportAnualDividends,
    FormUpdatePortofolio
  },
  data(){
    return{
      // Form New Company
      ImageNewCompany:'warehouse.png',
      TitleNewCompany:'New Company',

      // Form New Order
      ImageNewOrder:'securities.png',
      TitleNewOrder:'New Order',

      // Form Update Dividend
      ImageUpdateDividend:'profits.png',
      TitleUpdateDividend:'Update Company Dividend',

      // Form Portofolio Update
      ImagePortofolioUpdate:'candlestick.png',
      TitlePortofolioUpdate:'Update Portofolio',

      // Form Update Anual NAV
      ImageUpdateAnnualNAV:'growth.png',
      TitleUpdateAnnualNAV:'Update Annual NAV',

      // Form Import Anual Dividends
      ImageImportAnnualDividends:'AnualDividends.png',
      TitleImportAnnualDividends:'Import Annual Dividends',
    }
  },
  methods:{
  }
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>
.FormGroup{
  display:Flex;
}

h3{
  margin:15px;
}

</style>