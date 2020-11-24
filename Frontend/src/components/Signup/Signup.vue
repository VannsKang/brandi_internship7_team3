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
        <div class="signup-form">
          <div class="signup-form-title">가입 정보</div>

          <a-form-item>
            <a-input
              v-decorator="[
                'user_id',
                {
                  rules: [
                    { required: true, message: '필수 입력항목입니다.' },
                    { min: 5, message: '아이디의 최소 길이는 5글자입니다.' },
                    {
                      pattern: /^([A-Za-z0-9\uac00-\ud7af])+$/,
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
                      pattern: /^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[~!@#$%^&*()\-_=+,.<>/?;:[{}\]\\|]).{8,20}$/,
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

          <div class="signup-form-title">
            <span> 담당자 정보</span>
            <span>(*실제 샵을 운영하시는 분)</span>
          </div>

          <a-form-item>
            <a-input
              type="tel"
              v-decorator="[
                'owner_number',
                {
                  rules: [
                    {
                      required: true,
                      message: '올바른 정보를 입력해주세요.',
                    },
                    {
                      validator: checkNumberValid,
                      message: '올바른 정보를 입력해주세요.',
                    },
                  ],
                },
              ]"
              placeholder="핸드폰번호"
            >
              <a-icon
                slot="prefix"
                type="phone"
                style="color: rgba(0,0,0,.25)"
              />
            </a-input>
          </a-form-item>
          <div class="signup-form-extra">
            <a-icon type="info-circle" theme="filled" />
            <span
              >입점 신청 후 브랜디 담당자가 연락을 드릴 수 있으니 정확한 정보를
              기입해주세요.</span
            >
          </div>

          <div class="signup-form-title">셀러 정보</div>

          <a-form-item>
            <a-radio-group v-decorator="['seller_attribute_id']">
              <a-radio value="1">
                쇼핑몰
              </a-radio>
              <a-radio value="2">
                마켓
              </a-radio>
              <a-radio value="3">
                로드샵
              </a-radio>
              <a-radio value="4">
                디자이너브랜드
              </a-radio>
              <a-radio value="5">
                제너럴브랜드
              </a-radio>
              <a-radio value="6">
                내셔널브랜드
              </a-radio>
              <a-radio value="7">
                뷰티
              </a-radio>
            </a-radio-group>
          </a-form-item>
          <a-form-item>
            <a-input
              v-decorator="[
                'name',
                {
                  rules: [
                    { required: true, message: '필수 입력항목입니다.' },
                    { min: 1, message: '셀러명의 최소 길이는 1글자입니다.' },
                  ],
                },
              ]"
              placeholder="셀러명 (상호)"
            >
              <a-icon
                slot="prefix"
                type="font-size"
                style="color: rgba(0,0,0,.25)"
              />
            </a-input>
          </a-form-item>
          <a-form-item>
            <a-input
              v-decorator="[
                'eng_name',
                {
                  rules: [
                    { required: true, message: '필수 입력항목입니다.' },
                    {
                      min: 1,
                      message: '영문 상호명의 최소 길이는 1글자입니다.',
                    },
                    {
                      pattern: /^([A-Za-z0-9\uac00-\ud7af])+(\1?)$/,
                      message:
                        '영문 상호명은 1글자의 영문, 숫자, 언더바, 하이픈만 사용 가능하며 시작 문자는 영문 또는 숫자입니다.',
                    },
                  ],
                },
              ]"
              placeholder="영문 상호명"
            >
              <a-icon
                slot="prefix"
                type="font-size"
                style="color: rgba(0,0,0,.25)"
              />
            </a-input>
          </a-form-item>
          <a-form-item>
            <a-input
              v-decorator="[
                'cs_number',
                {
                  rules: [
                    {
                      required: true,
                      message: '올바른 정보를 입력해주세요.',
                    },
                    {
                      validator: checkNumberValid,
                      message: '올바른 정보를 입력해주세요.',
                    },
                  ],
                },
              ]"
              placeholder="고객센터 전화번호"
            >
              <a-icon
                slot="prefix"
                type="phone"
                style="color: rgba(0,0,0,.25)"
              />
            </a-input>
          </a-form-item>
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

export default {
  components: {
    "login-footer": loginFooter,
    "login-logo": loginLogo,
  },

  data() {
    return {
      confirmDirty: false,
    };
  },

  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "Signup" });
  },

  methods: {
    handleSubmit(e) {
      this.form.validateFieldsAndScroll((err, values) => {
        !err && console.log("Received values of form: ", values);
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

    checkNumberValid(rule, value, callback) {
      isNaN(+value) ? callback("It's not a number bro!") : callback();
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../../styles.scss";

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
    /* border: 1px solid red; */
    overflow: scroll;
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

    > div:nth-child(4) {
      margin-bottom: 35px;
    }

    .ant-form {
      &-item {
        margin-bottom: 8px;
      }
      /* &-explain */
    }

    &-title {
      font-size: 18px;
      font-weight: 700;
      margin-bottom: 5px;
      > span:last-child {
        font-size: 14px;
        font-weight: 400;
        color: rgb(30, 144, 255);
      }
    }

    &-extra {
      @include flexSet("flex-start", "center");
      margin: -10px 0 50px;
      font-size: 12px;
      font-weight: 600;
      color: rgb(30, 144, 255);

      > span {
        margin-left: 5px;
      }
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
