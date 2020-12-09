<template>
  <div class="main">
    <main-top />
    <a-layout class="main-sider">
      <main-side />
      <router-view />
    </a-layout>
    <main-footer />
  </div>
</template>

<script>
import { mapState } from "vuex";

// LINK component
import mainTop from "./Main-top/Main-top";
import mainSide from "./Main-side/Main-side";
import mainFooter from "./Main-footer/Main-footer";

export default {
  name: "Main",

  components: {
    "main-top": mainTop,
    "main-footer": mainFooter,
    "main-side": mainSide,
  },

  data() {
    return {};
  },

  computed: {
    ...mapState({
      user_token: ({ users }) => users.user_token,
    }),
  },

  mounted() {
    !this.user_token && this.$router.push("/403");
  },
};
</script>

<style src="./Main.scss" lang="scss" scoped />
