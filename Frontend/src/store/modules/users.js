import axios from "axios";
import Swal from "sweetalert2";

// LINK API
import { SIGNUP_API } from "../../config";

// SECTION initial state
const state = () => ({
  user_token: "",
  user_id: "",
});

// getters
const getters = {};

// mutations
const mutations = {
  getToken(state, payload) {
    state.user_token = payload.token;
    state.user_id = payload.user_id;
  },

  removeToken(state) {
    state.user_token = "";
    state.user_id = "";
  },
};

// actions
const actions = {
  getTokenAction({ commit }, payload) {
    commit("getToken", payload);
  },

  removeTokenAction({ commit }) {
    commit("removeToken");
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
