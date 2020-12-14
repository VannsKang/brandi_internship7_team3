<template>
  <a-layout-footer class="login-footer">
    <div>
      <div>
        <span>
          {{ footer_text }}
        </span>
        <span> {{ email }} | {{ copyright }} </span>
      </div>
      <div>
        <span>이용약관</span> |
        <span>개인정보처리방침</span>
      </div>
    </div>
  </a-layout-footer>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "Login-footer",

  mounted() {
    this.updateFooterAction();
  },

  computed: {
    ...mapState({
      footer_text: ({ navmenus }) => navmenus.footer_text,
      copyright: ({ navmenus }) => navmenus.copyright,
      email: ({ navmenus }) => navmenus.email,
    }),
  },

  methods: {
    ...mapActions("navmenus", ["updateFooterAction"]),
  },
};
</script>

<style src="./Login-footer.scss" lang="scss" scoped />
