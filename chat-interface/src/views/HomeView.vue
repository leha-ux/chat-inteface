<template>
  <MemberBar />
  <NotifyMessage />
  <ChatInterface v-if="showChatinterface"></ChatInterface>
  <EvaluationChat v-if="showEvaluation" />

</template>

<script>
/* eslint-disable */
import { mapGetters} from 'vuex' 
import AlertMessage  from '../components/Messages/AlertMessage.vue'
import NotifyMessage from '../components/Messages/NotifyMessage.vue'
import NavBar from '../components/NavBar.vue'
import MemberBar from '../components/MemberBar.vue'
import ChatInterface from '../components/ChatInterface.vue'
import LoginSignup from  '../components/LoginSignup.vue'
import EvaluationChat from  '../components/EvaluationChat.vue'


export default {
  name: 'HomeView',
  components: {NotifyMessage, AlertMessage, LoginSignup, NavBar, ChatInterface, EvaluationChat, MemberBar},

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