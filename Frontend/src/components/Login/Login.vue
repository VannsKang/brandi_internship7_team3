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
import { mapActions } from "vuex";

// LINK components
import loginLogo from "../components/Login-logo/Login-logo";
import loginFooter from "../components/Login-footer/Login-footer";

// LINK API
import { SIGNIN_API } from "../../config";

export default {
  name: "Login",

  components: {
    "login-footer": loginFooter,
    "login-logo": loginLogo,
  },

  data() {
    return {};
  },

  computed: {},

  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "normal_login" });
  },

  methods: {
    handleSubmit(e) {
      this.form.validateFields(async (err, values) => {
        // NOTE mockdata
        // !err && console.log("Received values of form: ", values);
        // if (!err) {
        //   const token = "thisismocktoken";
        //   console.log(token);
        //   this.getTokenAction({ token: token, user_id: values.user_id });
        //   this.$router.push("/main/seller");
        // }
        try {
          const response = await this.$http.post(SIGNIN_API, values);
          const validation = response && response.status === 200;
          !validation && new Error("cannot fetch the data");
          const { message, token } = response.data;
          console.log(message, values.user_id);
          this.getTokenAction({ token: token, user_id: values.user_id });
          message === "SUCCESS!" && this.$router.push("/main/seller");
        } catch (error) {
          console.log("!!error fetch data!!");
        }
      });
    },

    ...mapActions("users", ["getTokenAction"]),
  },
};
</script>

<style lang="scss">
@import "../../styles/mixin.scss";

.login {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background: $background-color;

  main {
    @include flexSet("center", "center", column);
    margin: auto;
    padding: 65px 0 50px;

    .login-template {
      width: 380px;
      padding: 64px 30px 0 30px;
      background: #fff;
      border-radius: 20px;
      box-shadow: 0 4px 31px 0 rgba(0, 0, 0, 0.1);

      form {
        .form-title {
          margin-bottom: 25px;
          font-weight: 700;
          font-size: 24px;
          text-align: left;
          line-height: 1.5;
          text-indent: 2px;
          letter-spacing: -1.5px;
        }

        .input-field {
          margin-bottom: 10px;

          .input-item {
            height: 46px;
            padding: 13px 16px;
            border-radius: 8px;
            line-height: 1.5;
            font-weight: 500;

            &::placeholder {
              color: #999;
              font-size: 12px;
            }
          }

          .ant-form-explain {
            text-align: left;
            margin-top: 5px;
            font-size: 12px;
            color: #000;
            font-weight: 700;
          }
        }

        .confirm-btn {
          width: 100%;
          height: 45px;
          margin-top: 10px;
          background: #000;
          border: #000;
          border-radius: 8px;
        }

        .signin-desc {
          font-size: 12px;
          color: #999;
        }
      }
    }
  }
}
</style>
