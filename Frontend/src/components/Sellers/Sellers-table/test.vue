<template>
  <div>
    <a-checkbox
      :indeterminate="indeterminate"
      :checked="checkAll"
      @change="onCheckAllChange"
    />

    <br />
    <a-checkbox-group
      v-model="checkedList"
      :options="plainOptions"
      @change="onChange"
    >
    </a-checkbox-group>
    <a-checkbox :options="plainOptions">dfsd</a-checkbox>
  </div>
</template>
<script>
const plainOptions = ["Apple", "Pear", "Orange"];
export default {
  data() {
    return {
      checkedList: [],
      indeterminate: false,
      checkAll: false,
      plainOptions,
    };
  },
  methods: {
    onChange(checkedList) {
      this.indeterminate =
        !!checkedList.length && checkedList.length < plainOptions.length;
      this.checkAll = checkedList.length === plainOptions.length;
    },
    onCheckAllChange(e) {
      Object.assign(this, {
        checkedList: e.target.checked ? plainOptions : [],
        indeterminate: false,
        checkAll: e.target.checked,
      });
    },
  },
};
</script>
