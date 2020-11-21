<template>
  <a-layout class="login">
    <a-layout-content>
      <a-row class="logo-section">
        <div class="logo">
          <img :src="logoImage" alt="" />
        </div>
      </a-row>
      <a-row class="login-template">
        <a-form
          id="components-form-demo-normal-login"
          :form="form"
          class="login-form"
          @submit="handleSubmit"
        >
          <h3 class="form-title">브랜디 어드민 로그인</h3>
          <a-form-item class="input-field">
            <a-input
              class="input-item"
              v-decorator="[
                'userName',
                {
                  rules: [
                    {
                      required: true,
                      message: '아이디를 입력해주세요.',
                    },
                  ],
                },
              ]"
              placeholder="셀러 아이디"
            >
            </a-input>
          </a-form-item>
          <a-form-item class="input-field">
            <a-input
              class="input-item"
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
              type="password"
              placeholder="셀러 비밀번호"
              autoComplete
            >
            </a-input>
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
              <a href="">
                회원가입하기
              </a>
            </span>
          </a-form-item>
        </a-form>
      </a-row>
    </a-layout-content>
    <login-footer />
  </a-layout>
</template>

<script>
import loginFooter from "./Login-footer/Login-footer";
import logoImage from "../../assets/logo_seller_admin.png";

export default {
  name: "Login",

  components: {
    "login-footer": loginFooter,
  },

  data() {
    return {
      logoImage,
    };
  },

  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "normal_login" });
  },

  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields((err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
        }
      });
    },
  },
};
</script>

<style lang="scss">
@import "../../styles.scss";

.login {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;

  main {
    @include flexSet("center", "center", column);
    margin: auto;
    padding: 65px 0 50px;

    .logo-section {
      @include flexSet("center", "center");

      .logo {
        width: 130px;
        margin-bottom: 40px;

        img {
          width: 100%;
        }
      }
    }

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
