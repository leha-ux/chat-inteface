<template>
  <AlertMessage />
    <NavBar />
  <LoginSignup v-if="!login"></LoginSignup>



</template>

<script>
/* eslint-disable */

import { mapGetters} from 'vuex'

import AlertMessage  from '../components/Messages/AlertMessage.vue'
import NotifyMessage from '../components/Messages/NotifyMessage.vue'
import NavBar from '../components/NavBar.vue'
import ChatInterface from '../components/ChatInterface.vue'
import LoginSignup from  '../components/LoginSignup.vue'
import EvaluationChat from  '../components/EvaluationChat.vue'


export default {
  name: 'LoginView',
  components: {NotifyMessage, AlertMessage, LoginSignup, NavBar, ChatInterface, EvaluationChat},

    computed: {
    ...mapGetters([
      'login',
      'showEvaluation',
      'showChatinterface',
      'roomMemberAvatar',
      'roomMemberName'

    ]),

  }
}
</script>
<style>

</style>