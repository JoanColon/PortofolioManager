<template>
  <div class="home">
     <div class="MyImageDiv">
      <h1>Welcome to your <strong>FIRE!</strong> platform</h1>
      <b-img :src="require('@/assets/homeStockMarket.jpg')" alt="Responsive image"></b-img>
      <h2>Financial Independence, Retire Early</h2>
    </div>  
  </div>
</template>

<script>
// import components


export default {
  name: 'HomeView',

}
</script>

<style scoped>
.MyImageDiv{
    margin-top: 200px;

}

img{
  height: 500px;
  width: 100%;
  display: block;
  margin: auto;
}

h1, h2{
  margin-top:25px; 
  text-align: center;
}

</style>
