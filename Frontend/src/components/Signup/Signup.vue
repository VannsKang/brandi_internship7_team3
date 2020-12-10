<template>
  <div class="signup">
    <section class="signup-main">
      <a-form :form="form" @submit.prevent="submitSignup">
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
          <signup-basic :form="form" />

          <signup-owner />

          <signup-seller />

          <a-form-item class="signup-form-button">
            <a-button type="primary" html-type="submit">
              신청
            </a-button>
            <a-button type="danger" @click="cancelSignup">
              취소
            </a-button>
          </a-form-item>
        </div>
      </a-form>
    </section>

    <login-footer />
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

// LINK components
import loginFooter from "../components/Login-footer/Login-footer";
import loginLogo from "../components/Login-logo/Login-logo";
import SignupBasic from "./Signup-basic/Signup-basic.vue";
import SignupOwner from "./Signup-owner/Signup-owner.vue";
import SignupSeller from "./Signup-seller/Signup-seller";

export default {
  components: {
    loginFooter,
    loginLogo,
    SignupBasic,
    SignupOwner,
    SignupSeller,
  },

  data() {
    return {};
  },

  computed: {
    ...mapState({
      user_token: ({ users }) => users.user_token,
    }),
  },

  // // SECTION lifecycle
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "Signup" });
  },

  mounted() {
    this.user_token && this.$router.push("/main/seller");
  },

  methods: {
    submitSignup() {
      this.form.validateFieldsAndScroll((err, values) => {
        this.signupAction({ err, values });
      });
    },

    async cancelSignup() {
      const swalWithBootstrapButtons = this.$alert.mixin({
        customClass: {
          confirmButton: "ant-btn ant-btn-primary",
          cancelButton: "ant-btn ant-btn-danger",
        },
        buttonsStyling: false,
      });

      const firstAlert = await this.$alert.fire({
        title: "회원가입",
        text: "브랜디 가입을 취소하시겠습니까?",
        icon: "question",
        showCancelButton: true,
        confirmButtonText: "예",
        cancelButtonText: "아니오",
        reverseButtons: true,
      });

      if (firstAlert.isConfirmed) {
        swalWithBootstrapButtons.fire({
          title: "회원 가입 취소 완료",
          text: "회원 가입이 취소되었습니다",
          icon: "warning",
          timer: 1000,
          showConfirmButton: false,
        });
        this.$router.push("/");
      }

      if (firstAlert.dismiss === this.$alert.DismissReason.cancel)
        return swalWithBootstrapButtons.fire({
          title: "회원 가입",
          text: "브랜디 가입을 진행해주세요",
          icon: "info",
          timer: 1000,
          showConfirmButton: false,
        });
    },
    ...mapActions("users", ["signupAction"]),
  },
};
</script>

<style src="./Signup.scss" lang="scss" scoped />
