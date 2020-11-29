<template>
  <div class="signup">
    <section class="signup-main">
      <a-form :form="form" @submit.prevent="handleSubmit">
        <login-logo />
        <div class="signup-title" align="center">
          <h3>셀러회원 가입</h3>
        </div>
        <div class="signup-subtitle">
          <div>
            정보입력
          </div>
        </div>

        <!-- SECTION signup -->
        <div class="signup-form">
          <div>
            <div class="signup-form-title">
              가입 정보
            </div>
            <a-form-item>
              <a-input
                v-decorator="[
                  'user_id',
                  {
                    rules: [
                      { required: true, message: '필수 입력항목입니다.' },
                      { min: 5, message: '아이디의 최소 길이는 5글자입니다.' },
                      {
                        pattern: /^([A-Za-z0-9])([A-Za-z0-9_-]){4,19}$/,
                        message:
                          '아이디는 5~20글자의 영문, 숫자, 언더바, 하이픈만 사용 가능하며 시작 문자는 영문 또는 숫자입니다.',
                      },
                    ],
                  },
                ]"
                placeholder="아이디"
              >
                <a-icon
                  slot="prefix"
                  type="user"
                  style="color: rgba(0,0,0,.25)"
                />
              </a-input>
            </a-form-item>
            <a-form-item has-feedback>
              <a-input
                v-decorator="[
                  'password',
                  {
                    rules: [
                      {
                        validator: validateToNextPassword,
                      },
                      {
                        pattern: /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[~!@#$%^&*()\-_=+,.<>/?;:[{}\]\\|]).{8,20}$/,
                        message:
                          '비밀번호는 8~20글자의 영문대소문자, 숫자, 특수문자를 조합해야 합니다.',
                      },
                    ],
                  },
                ]"
                type="password"
                placeholder="비밀번호"
                autocomplete
              >
                <a-icon
                  slot="prefix"
                  type="lock"
                  style="color: rgba(0,0,0,.25)"
                />
              </a-input>
            </a-form-item>
            <a-form-item has-feedback>
              <a-input
                v-decorator="[
                  'confirm_password',
                  {
                    rules: [
                      {
                        validator: compareToFirstPassword,
                        message: '비밀번호가 일치하지 않습니다.',
                      },
                    ],
                  },
                ]"
                type="password"
                placeholder="비밀번호 재입력"
                autocomplete
                @blur="handleConfirmBlur"
              >
                <a-icon
                  slot="prefix"
                  type="check"
                  style="color: rgba(0,0,0,.25)"
                />
              </a-input>
            </a-form-item>
          </div>

          <signup-owner />

          <signup-seller />

          <a-form-item class="signup-form-button">
            <a-button type="primary" html-type="submit">
              신청
            </a-button>
            <a-button type="danger">
              <router-link to="/" exact>
                취소
              </router-link>
            </a-button>
          </a-form-item>
        </div>
      </a-form>
    </section>

    <login-footer />
  </div>
</template>

<script>
import loginFooter from "../components/Login-footer/Login-footer";
import loginLogo from "../components/Login-logo/Login-logo";
import SignupOwner from "./Signup-owner/Signup-owner.vue";
import SignupSeller from "./Signup-seller/Signup-seller";
import { SIGNUP_API } from "../../config";

export default {
  components: {
    "login-footer": loginFooter,
    "login-logo": loginLogo,
    "signup-owner": SignupOwner,
    "signup-seller": SignupSeller,
  },

  data() {
    return {
      confirmDirty: false,
    };
  },

  // SECTION lifecycle
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "Signup" });
  },

  methods: {
    handleSubmit() {
      this.form.validateFieldsAndScroll(async (err, values) => {
        // REVIEW for data check
        // !err && console.log("Received values of form: ", values);
        try {
          const response = await this.$http.post(SIGNUP_API, values);
          const validation = response && response.status === 200;
          !validation && new Error("cannot fetch the data");
          const { message } = response.data;
          console.log(message, values);
          message === "SUCCESS" && this.$router.push(`/`);
        } catch (error) {
          console.log("!!error fetch data!!");
        }
      });
    },

    handleConfirmBlur(e) {
      const { value } = e.target;
      this.confirmDirty = this.confirmDirty || !!value;
    },

    validateToNextPassword(rule, value, callback) {
      const { form } = this;
      value &&
        this.confirmDirty &&
        form.validateFields(["confirm"], { force: true });
      callback();
    },

    compareToFirstPassword(rule, value, callback) {
      const { form } = this;
      value && value !== form.getFieldValue("password")
        ? callback("not matched!")
        : callback();
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../../styles/mixin.scss";

.signup {
  position: absolute;
  background: $background-color;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  @include flexSet("space-between", "center", "column");

  &-main {
    background: #fff;
    width: 500px;
    margin: 0 auto;
    padding: 20px 30px 15px;
    border-radius: 4px;
    overflow-y: scroll;
    overflow-x: hidden;
    > form {
      width: 100%;
    }
  }

  &-title h3 {
    font-size: 24px;
    margin-bottom: 15px;
  }

  &-subtitle {
    border-top: 1px solid #ddd;
    width: 100%;
    padding-top: 20px;
    margin-bottom: 20px;
    @include flexSet("center", "center");

    > div {
      width: 408px;
      height: 45px;
      background: $primary-color;
      color: #ddd;
      font-size: 20px;
      font-weight: 500;
      @include flexSet("center", "center");
    }
  }

  &-form {
    width: 408px;
    margin: 0 auto;

    > div {
      margin-bottom: 35px;
    }

    .ant-form {
      &-item {
        margin-bottom: 8px;
      }
    }

    &-title {
      font-size: 18px;
      font-weight: 700;
      margin-bottom: 5px;
    }

    &-button {
      margin-top: 40px;
      @include flexSet("center", "center");
      button {
        padding: 0 10px;
        &:first-child {
          border-top-right-radius: 0;
          border-bottom-right-radius: 0;
          background: $confirm-color;
        }

        &:last-child {
          border-top-left-radius: 0;
          border-bottom-left-radius: 0;
          margin-left: -1px;
          background: $reject-color;
        }
      }
    }
  }
}
</style>
