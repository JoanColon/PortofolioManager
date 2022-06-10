<!------------------------------------------------------------------------>
<!------------------------- Templates ------------------------------------>
<!------------------------------------------------------------------------>
<template>
<div>
  <b-card no-body class="overflow-hidden" style="card">
    <b-row no-gutters>
      <b-card-img 
        :src="require('@/assets/' + imageName + '')" 
        alt="Image" 
        class="carc-img rounded-0">
      </b-card-img>
    </b-row>
    <b-row>
      <b-card-body :title="title">
        <!-- <b-card-text >
          <h4 class="card-text">{{data}}</h4>
        </b-card-text> -->
      </b-card-body>
    </b-row>
  </b-card>
</div>
</template>

<!------------------------------------------------------------------------>
<!--------------------------- Scripts ------------------------------------>
<!------------------------------------------------------------------------>
<script>
export default {
  name:'BaseCardDataManag',
  props:['title','imageName'],
}
</script>

<!------------------------------------------------------------------------>
<!---------------------------- Styles ------------------------------------>
<!------------------------------------------------------------------------>
<style scoped>
.card{
  margin-left: 25px;
  margin-right: 25px;
  margin-bottom: 25px;
  width: 150px;
  height:200px;
  box-shadow: 5px 5px #888888;
}

.card-img{
  height:100px;
  width:100px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}

.card-body{
  white-space: wrap;  /* makes teh text to fit in several line */
  text-align: center;
}

.card-text{
  font-weight: bold;
}

</style>