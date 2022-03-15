import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

// ------------------------------------------------------------------
// ----------------- views imports ----------------------------------
// ------------------------------------------------------------------
import HomeView from '../views/HomeView.vue'
import ViewPortofolio from '../views/ViewPortofolio.vue'
import ViewDividends from '../views/ViewDividends.vue'
import ViewStockAnalysis from '../views/ViewStockAnalysis.vue'
import AboutView from '../views/AboutView.vue'

// ------------------------------------------------------------------
// ------------------ views configuration ---------------------------
// ------------------------------------------------------------------
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/portofolio',
    name: 'portofolio',
    component: ViewPortofolio
  },
  {
    path: '/dividends',
    name: 'dividends',
    component: ViewDividends
  },
  {
    path: '/stockanalysis',
    name: 'sotckanalysis',
    component: ViewStockAnalysis
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  }
]

// ------------------------------------------------------------------
// ------------------ router configuration --------------------------
// ------------------------------------------------------------------
const router = new VueRouter({
  routes
})

export default router
