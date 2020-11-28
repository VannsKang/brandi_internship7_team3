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
};
</script>

<style lang="scss" scoped>
@import "../../styles/mixin.scss";

.main {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;

  &-sider {
    min-height: calc(100% - 96px);
  }
}
</style>
