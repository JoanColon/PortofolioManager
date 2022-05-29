<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div class="dividends">
<h3>General Forms</h3>
<FormNewCompany/>

<FormNewOrder/>

<h3>Portofolio forms</h3>
<FormUpdatePortofolio/>

<h3>Historic Performance forms</h3>

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
h3{
  margin-left: 10px;
}

</style>