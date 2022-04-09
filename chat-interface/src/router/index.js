/* eslint-disable */

import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import store from '../store/index.js'

 


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      requiresLogin: true
    },
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: "/:catchAll(.*)",
    redirect: to => {
      return '/'
    },
  }
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresLogin)) {
    if(!store.getters.login){
      next("/login")
    }    else {
      next()
    }
  } else {
      next()
  }
})



export default router
