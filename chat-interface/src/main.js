import { createApp } from 'vue'
import Vant from 'vant';
import 'vant/lib/index.css';
import App from './App.vue'
import store from './store'

import './main.css'

import VueSocketIO from 'vue-3-socket.io'
import SocketIO from 'socket.io-client'

import naive from 'naive-ui'

import { Dialog } from 'vant';
import router from './router'




createApp(App).use(router).use(store).use(new VueSocketIO({
    debug: true,
    connection: SocketIO('localhost:8084', {autoConnect: false}), //options object is Optional
    vuex: {
      store,
      actionPrefix: "SOCKET_",
      mutationPrefix: "SOCKET_"
    }
  })
).use(naive).use(Vant).use( Dialog ).mount('#app')