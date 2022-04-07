<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div class="dividends">
  <h3>Enter and modify portofolio data</h3>

  <FormNewCompany/>

  <FormNewOrder/>

  <FormUpdatePortofolio/>

</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
// import components
import FormNewCompany from '@/components/FormNewCompany.vue' //@ redirects to src folder
import FormNewOrder from '@/components/FormNewOrder.vue'
import FormUpdatePortofolio from '@/components/FormUpdatePortofolio.vue'  

export default {
  name: 'ViewDataManagement',
  components: {
    FormNewCompany,
    FormNewOrder,
    FormUpdatePortofolio
  },
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>

</style>