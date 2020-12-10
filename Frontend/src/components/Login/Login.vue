<template>
  <a-layout class="login">
    <a-layout-content>
      <login-logo />
      <a-row class="login-template">
        <a-form
          id="components-form-demo-normal-login"
          :form="form"
          class="login-form"
          @submit.prevent="handleSubmit"
        >
          <h3 class="form-title">
            브랜디 어드민 로그인
          </h3>
          <a-form-item class="input-field">
            <a-input
              v-decorator="[
                'user_id',
                {
                  rules: [
                    {
                      required: true,
                      message: '아이디를 입력해주세요.',
                    },
                  ],
                },
              ]"
              class="input-item"
              placeholder="셀러 아이디"
            />
          </a-form-item>
          <a-form-item class="input-field">
            <a-input
              v-decorator="[
                'password',
                {
                  rules: [
                    {
                      required: true,
                      message: '비밀번호를 입력해주세요.',
                    },
                  ],
                },
              ]"
              class="input-item"
              type="password"
              placeholder="셀러 비밀번호"
              autocomplete
            />
          </a-form-item>

          <a-form-item>
            <a-button
              type="primary"
              html-type="submit"
              class="login-form-button confirm-btn"
            >
              로그인
            </a-button>
            <span class="signin-desc">
              아직 셀러가 아니신가요?
              <router-link to="/signup" exact>
                회원가입하기
              </router-link>
            </span>
          </a-form-item>
        </a-form>
      </a-row>
    </a-layout-content>
    <login-footer />
  </a-layout>
</template>

<script>
import { mapActions, mapState } from "vuex";

// LINK components
import loginLogo from "../components/Login-logo/Login-logo";
import loginFooter from "../components/Login-footer/Login-footer";

export default {
  name: "Login",

  components: {
    loginFooter,
    loginLogo,
  },

  data() {
    return {};
  },

  computed: {
    ...mapState({
      user_token: ({ users }) => users.user_token,
    }),
  },

  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "Login" });
  },

  mounted() {
    this.user_token && this.$router.push("/main/seller");
  },

  methods: {
    handleSubmit() {
      this.form.validateFields((err, values) => {
        this.signinAction({ err, values });
      });
    },

    ...mapActions("users", ["getTokenAction", "signinAction"]),
  },
};
</script>

<style src="./Login.scss" lang="scss" />
