// ----------------------------------------------------------------------------
// ------------------------ TEMPLATES -----------------------------------------
// ----------------------------------------------------------------------------
<template>
  <div id="app">
    <!-- Header component -->
    <TheHeader/>

    <!-- The Navbar and router-links to views -->
      <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/portofolio">Portofolio</router-link> |
      <router-link to="/historicperformance">Historic Performance</router-link> |
      <router-link to="/stockanalysis">Stock Analysis</router-link> |
      <router-link to="/datamanagement">Data Management</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>

    <!-- Other components -->
  </div>
</template>

// ----------------------------------------------------------------------------
// ------------------------------ SCRIPT --------------------------------------
// ----------------------------------------------------------------------------
<script>
// import components
import TheHeader from '@/components/TheHeader.vue' //@ redirects to src folder

export default {
  name: 'App',
  components: {
    TheHeader,
  }
}
</script>

// ----------------------------------------------------------------------------
// ------------------------------ SCRIPT --------------------------------------
// ----------------------------------------------------------------------------
<script>
// import components
import TheHeader from '@/components/TheHeader.vue' //@ redirects to src folder

export default {
  name: 'App',
  components: {
    TheHeader,
  }
}
</script>

// ----------------------------------------------------------------------------
// ------------------------------ STYLES --------------------------------------
// ----------------------------------------------------------------------------
<style scoped>
#app {
  margin: 0px;
  padding: 0px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

nav {
  margin-left: 0px;
  margin-right: auto;
  padding: 10px;
  background-color: #333;
}

nav a {
  font-weight: bold;
  color: white;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>