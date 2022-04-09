/* eslint-disable */

import { createStore } from 'vuex'
import { getField, updateField } from 'vuex-map-fields'
import axios from 'axios';
import router from '../router'


export default createStore({
  state: {
    avatar: {'topValue' : null,
    'skinColorValue' : null, 
    'accessoriesValue' : null,
    'hairColorValue' : null,
    'facialhairTypeValue' : null,
    'eyeTypeValue' : null,
    'eyebrowValue' : null,
    'mouthValue' : null, 
    'facialHairColorValue' : null, 
    'clotheTypeValue' : null,
    'clotheColorValue' : null,
    'eyeColorValue' : null,
    },
    message: "",
    accessToken: null,
    error: "",
    messages: [],
    user: {},
    room: {},
    selected: "",
  },
  getters: {
//----------------------------GETTERS-------------------------------
getField,
messageEmpty: (state) => {
  var messageHelp = state.message
  messageHelp = messageHelp.trim()
  if(messageHelp!=""){
    return false
  } else {return true}
},
  messages: state => {return state.messages},
  login: state => {return  state.accessToken != null},
  message: state=> {return state.message},
  selected: state=> {return state.selected},
  error:  state=> {return state.error},
  currentUser: state => {return state.user.name},
  currentUserAvatar: state => {return state.user.avatar},
  roomMemberName: state => {
    if('user' in state.room){
      const userInRoomByName = state.room.user.map(x => x.name)
      const result = userInRoomByName.filter(user => user!=state.user.name)
      return result[0]
    }},
  
  roomMemberAvatar: state => {
    if('user' in state.room){
      const userInRoomByName = state.room.user.map(x => x.name)
      const result = userInRoomByName.filter(user => user!=state.user.name)
      return state.room.user.find( user => user.name === result[0]).avatar
    }},

//--------------------------------SHOW COMPONENTS------------------------------
  showWait: state => {
    if(!!state.accessToken){
      if(!('user' in state.room)){
        return true
      }  else if(state.room["evaluated_by"].includes(state.user.name)){
        return true
      } else {
        return false
      }
    } else {
      return false
    }
  },
  showChatinterface: state => {
    if(!!state.accessToken && state.room.hasOwnProperty("depreciated")){
      if(!state.room["depreciated"] && !state.room["evaluation_complete"] && !state.room["evaluated"]){
        alert("showChat")
        return true
      } else {
        return false
      }
    } else {
      return false
    } },
  showEvaluation: state => {
    if(state.room["depreciated"] && !state.room["evaluation_complete"] && !state.room["evaluated"] && !state.room["evaluated_by"].includes(state.user.name)){
      return true
    } else {
      return false
    }
  }
  },

  mutations: {
    updateField,

//----------------------------------------TOKEN-------------------------------------------

SET_TOKEN (state,access) {
  state.accessToken = access
},

DESTROY_TOKEN (state) {
  state.accessToken = null
},

//-----------------------------------------------------------------------------------

    SET_AVATAR(state, avatar){
    state.avatar = avatar
    },
    SET_MESSAGES (state, messages){
      console.log("MESSAGES" + JSON.stringify(messages))
      state.messages = messages
    },
    SET_USER (state, user) {
      state.user = user
    },

    SET_ROOM (state, room) {
      console.log("ROOM" + JSON.stringify(room))
      if(room==null){
        state.room= {}
      } else {
        state.room=room
      }
    },

    CLEAR_USER (state) {
      state.user = null
    },

    SET_ERROR(state, error){
      state.error = error 
    },

    SET_SELECTED(state, selected){
      state.selected = selected       
    },


  },
  actions: {
//-----------------------------------------SOCKET------------------------------------------

    EMIT_EVALUATION(context, data){
      const socket = (data["socket"])
      socket.emit('SEND_EVALUATION', {name: context.state.user.name, eval: data["evaluation"]})
    },

    EMIT_MESSAGE (context, socket) {
      if (context.state.message!=""){
      socket.emit('SEND_MESSAGE', {text: context.state.message.trim(), name: context.state.user.name})
      context.state.message = ""
    }
    },
    SOCKET_DATA (context, data) {
      if (data["messages"].length > 0){
      context.commit('SET_MESSAGES', JSON.parse(data["messages"]))}
      context.commit('SET_ROOM', JSON.parse(data["room"]))
  },

  //------------------------------------AUTHENTIFICATION / Web Server ------------------------------------

    login (context, data) {
      const socket = (data["socket"])
      axios
      .post('https://authent.azurewebsites.net/login',
      {"name" : data["name"], "password" : data["password"]},
            {headers: {"Content-Type": "application/json"}})
      .then((response) => {
        context.commit('SET_USER', (response.data.user))
        context.commit('SET_TOKEN', response.data.token)
        socket.io.opts.query = {
          access_token: response.data.token,
        };
        socket.connect()
        router.push('/')

        socket.emit('LOGIN', {name: (response.data.user.name)})
      })
      .catch((error) => {
        context.commit('SET_ERROR', (error.response.data.error))
      });
    },
    signup (context, data) {
      const socket = (data["socket"])
      axios
      .post('https://authent.azurewebsites.net/signup',
      {"name" : data["name"], "password" : data["password"], "avatar" : context.state.avatar},
            {headers: {"Content-Type": "application/json"}})
      .then((response) => {
        context.commit('SET_USER', (response.data.user))
        context.commit('SET_TOKEN', response.data.token)
        router.push('/')
        socket.io.opts.query = {
          access_token: response.data.token,
        };
        socket.connect()
        socket.emit('LOGIN', {name: response.data.user.name})
      })
      .catch((error) => {
          context.commit('SET_ERROR', (error.response.data.error))
      });
    },
  
  logout (context, socket) {
    context.commit('DESTROY_TOKEN')
    context.commit('SET_USER', "")
    context.commit('SET_ROOM', {})
    socket.disconnect()
  },
    
  },
  modules: {
  }
})