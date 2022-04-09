<template>
  <n-config-provider :theme-overrides="themeOverrides">

<div class="container-sm mt-40">
<n-card>
<van-notify v-model:show="error" type="danger">
<van-icon name="bell" style="margin-right: 4px;" />
<span>Please fill out all fields</span>
</van-notify>
<van-notify v-model:show="success" type="success">
<van-icon name="bell" style="margin-right: 4px;" />
<span>Evaluation successful submitted</span>
</van-notify>
<van-steps :active="active" active-icon="success" active-color="#38f">
  <van-step>Human/Bot</van-step>
  <van-step>Messages</van-step>
  <van-step>Further Metrics...</van-step>
</van-steps>
<n-grid v-if="page===1"  :y-gap="20"  :cols="2">
    <n-gi>
      <h1>1. Do you think your chat partner was a human or a bot?</h1>
    </n-gi>
    <n-gi>
      <div class="flex items-center justify-center">

  
  <n-radio-group
  size="small"
    v-model:value="humanbot"
    name="humanorbot"
    style="margin-bottom: 12px"
  >
    <n-radio-button 
    type="info"
    value="human"
    class="text-sky-600 focus:bg-blue-500"
    >
      Human
    </n-radio-button>
    <n-radio-button 
    value="bot"
    type="info"
    class="text-sky-600 focus:bg-blue-500"
    >
      Bot
    </n-radio-button>
  </n-radio-group>

      </div>
    </n-gi>
        <n-gi>
      <h1>2. How confident are you in your answer to question 1?</h1>
    </n-gi>
    <n-gi class="ml-4 grid">
  <h1 class="text-left">very confident</h1>
<van-radio-group class="ml-10 mt-2 mb-2" v-model="checked" direction="horizontal">
  <van-radio name="1"></van-radio>
  <van-radio name="2"></van-radio>
    <van-radio name="3"></van-radio>
  <van-radio name="4"></van-radio>
    <van-radio name="5"></van-radio>
    <van-radio name="6"></van-radio>
</van-radio-group>
<h1 class="text-right">not confident</h1>
  </n-gi>
  </n-grid>
  <div v-if="page===2">
      <h1>3. Please select the message, you attribute the decision made in 1. most likely to.</h1>
      <EvalSingleMessage @clicked="setMessageEvaluation" class="mt-20"
        v-for="{ _id, text, user_name} in messages"
        :key="_id.$oid"
        :id="_id.$oid"
        :text="text"
        :name="user_name"
        :sender="user_name=== currentUser"
        :selectedMessage="selected=== _id.$oid"
      >
        {{ text }}
      </EvalSingleMessage>
  </div>
  <n-grid class="mt-8" x-gap="12" :cols="3">
    <n-gi span="2">
      <div class="flex items-end justify-end">
    <n-pagination class="text-blue-500" @change="pageHandler" v-model:page="page" :page-count="3" />
      </div>
    </n-gi>
    <n-gi>
      <div class="flex items-end justify-end">
        <n-button @click="submit" size="small" type="info" ghost>Submit</n-button>
      </div>
    </n-gi>
  </n-grid>

</n-card>
  </div>
    </n-config-provider>
</template>

<script> 
/* eslint-disable */
import { watch, ref, computed, getCurrentInstance } from 'vue';
import { useStore } from 'vuex'
import EvalSingleMessage from './EvalSingleMessage.vue'
import { NConfigProvider } from 'naive-ui'

  /**
   * Use this for type hints under js file
   * @type import('naive-ui').GlobalThemeOverrides
   */




export default {
components: { EvalSingleMessage },
  setup() {



  const themeOverrides = {
    common: {
      primaryColor: '#1a89fa'
    },
    Button: {
      textColor: '#1a89fa'
    },
    Select: {
      peers: {
        InternalSelection: {
          textColor: '#1a89fa'
        }
      }
    }
  }

const store = useStore()
const globals = getCurrentInstance().appContext.config.globalProperties;
const checked = ref('1');
const active = ref(0);
const page = ref(1);
const humanbot = ref('')
const messageevaluation = ref('')
const error = ref(false)
const success = ref(false)
const setMessageEvaluation = (value) => {
messageevaluation.value = value
};
const pageHandler = () => {
  active.value = page.value-1
};


const submit = () => {
let form = {bot_human : humanbot.value, confidence : checked.value, message : messageevaluation.value}
console.log(JSON.stringify(form))
if(humanbot.value!="" && checked.value!="" && messageevaluation.value!=""){
store.dispatch('EMIT_EVALUATION', {'evaluation' : form, 'socket' : globals.$socket})
}
error.value = humanbot.value!="" && checked.value!="" && messageevaluation.value!=""  ? false : true
success.value = humanbot.value!="" && checked.value!="" && messageevaluation.value!=""  ? true : false
setTimeout(() => {
  success.value = false
  error.value = false;
}, 3000);
};

  return {
    themeOverrides,
    success,
    error, 
    setMessageEvaluation,
    humanbot,
    messageevaluation, 
    messages: computed(() => store.state.messages),
    selected: computed(()=>store.state.selected),
    currentUser: computed(() => store.state.user.name),
    pageHandler,
    checked,
    page,
    active,
    submit,
    };

  },
};
</script>