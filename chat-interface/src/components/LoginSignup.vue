<template>
<div class="container-sm mt-40">
  <van-notify v-model:show="show" type="danger">
  <van-icon name="bell" style="margin-right: 4px;" />
  <span>{{errorMessage}}</span>

</van-notify>
  <n-card>
    <n-tabs type="segment" default-value="signin" size="large">
      <n-tab-pane name="signin" tab="Sign in">
<van-form @submit="onLogin">
  <van-cell-group>
    <van-field
      clearable
      label-width="10em"
      v-model="username"
      name="Username"
      label="Username"
      placeholder="Username"
      :rules="[{ required: true, message: 'Username is required' }]"
    />
    <van-field
    clearable
      v-model="password"
      label-width="10em"
      type="password"
      name="Password"
      label="Password"
      placeholder="Password"
      :rules="[{ required: true, message: 'Password is required' }]"
    />
  </van-cell-group>
  <div style="margin: 16px;">
    <van-button round block plain type="primary" native-type="submit">
      Login
    </van-button>
  </div>
</van-form>
      </n-tab-pane>
      <n-tab-pane name="register" tab="Register">
<van-form @submit="onRegister"  >
  <van-cell-group large >
    <van-field
    clearable
    label-width="10em"
      v-model="usernameRegister"
      name="Username"
      label="Username"
      placeholder="Username"
      :rules="[{ required: true, message: 'Username is required' }]"
    />
    <van-field
      clearable
      v-model="passwordRegister"
      label-width="10em"
      type="password"
      name="Password"
      label="Password"
      placeholder="Password"
      :rules="[{ required: true, message: 'Password is required' }, {validator: checkLength, message: 'Password needs to have at least 10 characters'}]"
    />
      <van-field
      clearable
      v-model=" reenterRegisterPassword"
      label-width="10em"
      type="password"
      name="reenterPassword"
      label="Reenter Password"
      placeholder="Reenter Password"
      :rules="[{ required: true, message: 'Password is required' }, {validator: checkLength, message: 'Password needs to have at least 10 characters'}, { validator: checkPassword, message: 'Passwords do not match' }]"
    />
  </van-cell-group>
  <AvatarInput/>
  <div style="margin: 16px;">
    <van-button round block plain type="primary" native-type="submit">
      Register
    </van-button>
  </div>
</van-form>
      </n-tab-pane>
    </n-tabs>
  </n-card>
  </div>
</template>

<script> 
/* eslint-disable */
import { watch, ref, computed, getCurrentInstance } from 'vue';
import { useRouter} from 'vue-router'

import { useStore } from 'vuex'
import AvatarInput from './AvatarInput.vue'



export default {
components: { AvatarInput },
  setup() {
    const router = useRouter()
    const store = useStore()
    const globals = getCurrentInstance().appContext.config.globalProperties;
    const username = ref('');
    const usernameRegister = ref('');
    const password = ref('');
    const passwordRegister = ref('');
    const reenterRegisterPassword = ref('');
    const errorMessage = ref('')
    const show = ref(false);

    const onRegister = (values) => {
    store.dispatch('signup', {'name' : usernameRegister.value,'password' : passwordRegister.value, 'socket' : globals.$socket})
    };
    const onLogin = (values) => {
      store.dispatch('login', {'name' : username.value,'password' : password.value, 'socket' : globals.$socket, 'router' : router})
      };

    const checkPassword = function(val) {
      console.log(password.value)
    if(passwordRegister.value!=reenterRegisterPassword.value){
        return false
    };
    }

    const checkLength = function(val) {
    if(val.length<5){
        return false
    };
    }

    return {
      username,
      usernameRegister,
      password,
      passwordRegister,
      reenterRegisterPassword,
      errorMessage,
      checkLength, 
      avatar: computed(() => store.state.avatar),
      onLogin,
      onRegister,
      checkPassword,
    };
  },
};
</script>