import axios from "axios";
import Swal from "sweetalert2";
import { router } from "../../main";

// LINK API
import { SIGNUP_API, SIGNIN_API } from "../../config";

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

  async signinAction({ commit }, payload) {
    if (payload.err)
      return Swal.fire({
        title: "잘못된 로그인 시도입니다!",
        text:
          "혹시 처음이신가요? 여성복 쇼핑몰 브랜디에 가입해서 다양한 상품을 만나보세요!",
        timer: 2000,
        icon: "error",
        showConfirmButton: false,
      });

    try {
      // NOTE mockdata
      // const response = await this.$http.get(SIGNIN_API);

      // NOTE backend
      const response = await axios.post(SIGNIN_API, payload.values);
      console.log(response, "!!!!!!!!!!!!!!!!!!!!!");
      const validation = response && response.status === 200;
      !validation && new Error("cannot fetch the data");
      const { message, token } = response.data;
      console.log(message, payload.values.user_id);

      // NOTE get token
      actions.getTokenAction(
        { commit },
        { token: token, user_id: payload.values.user_id }
      );
      if (message === "SUCCESS!")
        return Swal.fire(
          {
            title: "로그인 성공!",
            timer: 2000,
            icon: "success",
            showConfirmButton: false,
          },
          router.push("/main/seller")
        );
    } catch (error) {
      console.log(`!!error fetch data!!: ${error.response.data.message}`);
      if (
        error.response.data.message === "아이디와 비밀번호를 다시 확인해주세요."
      )
        return Swal.fire({
          title: "비밀번호 오류!",
          text: "비밀번호를 다시 확인해주세요!",
          timer: 2000,
          icon: "error",
          showConfirmButton: false,
        });

      Swal.fire({
        title: "존재하지 않는 회원입니다!",
        timer: 2000,
        icon: "error",
        showConfirmButton: false,
      });
    }
  },

  async signupAction({ commmit }, payload) {
    if (payload.err)
      return Swal.fire({
        title: "필수 항목을 입력해주세요!",
        timer: 1000,
        icon: "error",
        showConfirmButton: false,
      });
    try {
      // ANCHOR mockdata
      // const response = await this.$http.get(SIGNUP_API);

      // ANCHOR backend
      const response = await axios.post(SIGNUP_API, payload.values);
      const validation = response && response.status === 200;
      !validation && new Error("cannot fetch the data");
      const { message } = response.data;
      console.log(message, payload.values);
      if (message === "SUCCESS") {
        Swal.fire({
          title: "회원 가입 완료",
          timer: 1000,
          icon: "success",
          showConfirmButton: false,
        });
        router.push(`/`);
      }
    } catch (error) {
      console.log("!!error fetch data!!");
      Swal.fire({
        title: "이미 가입된 사용자입니다.",
        timer: 1000,
        icon: "error",
        showConfirmButton: false,
      });
    }
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions,
};
