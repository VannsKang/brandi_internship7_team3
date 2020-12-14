<template>
  <a-row class="logo-section">
    <div class="logo">
      <router-link to="/" exact>
        <img :src="logoImage" alt="" />
      </router-link>
    </div>
  </a-row>
</template>

<script>
import logoImage from "../../../assets/logo_seller_admin.png";

export default {
  name: "Login-logo",

  data() {
    return {
      logoImage,
    };
  },
};
</script>

<style src="./Login-logo.scss" lang="scss" scoped />
