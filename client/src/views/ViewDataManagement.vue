<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
  <h3>General Forms</h3>
  <div class="FormGroup" id="GeneralForms">
    <!-- New Company -->
    <BaseCardDataManag
      :imageName='ImageNewCompany'
      :title='TitleNewCompany'
      v-b-modal.modalNewCompany
    />

    <b-modal id="modalNewCompany" title="Add a new Company">
      <FormNewCompany/>
    </b-modal>

    <!-- New Order -->
    <BaseCardDataManag
      :imageName='ImageNewCompany'
      :title='TitleNewOrder'
      v-b-modal.modalNewOrder
    />

    <b-modal id="modalNewOrder" title="Add a new Order">
      <FormNewOrder/>
    </b-modal>
  </div>


<h3>Portofolio forms</h3>
<FormUpdatePortofolio/>

<h3>Historic Performance forms</h3>
<FormImportAnualDividends/>

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
      ImageNewCompany:'Portofolio.png',
      TitleNewCompany:'New Company',

      ImageNewOrder:'Portofolio.png',
      TitleNewOrder:'New Order'
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