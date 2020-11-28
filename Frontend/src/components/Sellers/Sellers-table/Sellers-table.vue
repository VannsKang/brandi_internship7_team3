<template>
  <div class="sellers-content-main-table">
    <table>
      <!-- SECTION table header -->

      <thead>
        <tr>
          <th>
            <div>
              <a-checkbox
                :indeterminate="indeterminate"
                :checked="checkAll"
                @change="onCheckAllChange"
              />
            </div>
          </th>
          <th v-for="column in columns" :key="column.dataIndex">
            <div>
              {{ column.title }}
            </div>
          </th>
        </tr>
      </thead>
      <tbody>
        <!-- SECTION search row -->

        <tr>
          <td></td>

          <td
            v-for="col in [
              'seller_key',
              'seller_id',
              'seller_name_eng',
              'seller_name',
              'owner_name',
            ]"
            :key="col"
          >
            <div>
              <a-input @keyup.enter="searchInput" :id="col" />
            </div>
          </td>

          <td>
            <div>
              <a-select
                default-value="Select"
                style="width: 80px"
                @change="searchSellerStatus"
              >
                <a-select-option
                  v-for="stat in seller_status"
                  :value="stat.name"
                  :key="stat.id"
                >
                  {{ stat.name }}
                </a-select-option>
              </a-select>
            </div>
          </td>

          <td v-for="col in ['owner_phone', 'owner_email']" :key="col">
            <div>
              <a-input @keyup.enter="searchInput" :id="col" />
            </div>
          </td>

          <td>
            <div>
              <a-select
                default-value="Select"
                style="width: 100px"
                @change="searchSellerId"
              >
                <a-select-option
                  v-for="attribute in seller_attribute_id"
                  :value="attribute.id"
                  :key="attribute.id"
                >
                  {{ attribute.name }}
                </a-select-option>
              </a-select>
            </div>
          </td>
          <td>
            <div>
              <a-date-picker placeholder="From" @change="onDateChange" />
              <a-date-picker placeholder="to" @change="onDateChange" />
            </div>
          </td>
          <td>
            <div>
              <a-button type="primary">
                <a-icon type="search" />
                <span>Search</span>
              </a-button>
              <a-button type="primary">
                <a-icon type="close" />
                <span>Reset</span>
              </a-button>
            </div>
          </td>
        </tr>

        <!-- SECTION data row -->

        <tr v-for="item in data" :key="item.id">
          <td>
            <div>
              <a-checkbox
                class="listItems"
                @change="changeEachCheckBox"
                :id="item.id.toString()"
              />
            </div>
          </td>

          <td>
            <div>
              {{ item.id }}
            </div>
          </td>

          <td>
            <div @click="moveSellerDetails" :id="item.id">
              {{ item.seller_id }}
            </div>
          </td>

          <template v-for="(val, name, index) in item">
            <td v-if="index > 1 && name !== 'seller_actions'" :key="name">
              <div>
                {{ val }}
              </div>
            </td>
          </template>

          <td>
            <span>
              <a-button
                :key="idx"
                v-for="(btn, idx) in item.seller_actions"
                :style="confirmBtnColor(btn)"
              >
                {{ btn }}
              </a-button>
            </span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "Sellers-table",

  components: {},

  props: {
    data: {
      type: Array,
      required: true,
    },
    columns: {
      type: Array,
      required: true,
    },
    seller_status: {
      type: Array,
      required: true,
    },
    seller_attribute_id: {
      type: Array,
      required: true,
    },
  },

  data() {
    return {
      // ANCHOR for list control
      indeterminate: false,
      checkAll: false,
      plainOptions: [],
      checkedList: [],

      // ANCHOR for input items
    };
  },

  methods: {
    // ANCHOR checkbox control
    changeEachCheckBox(e) {
      const { checked, id } = e.target;

      if (checked) {
        this.checkedList = [...this.checkedList, +id];
      } else {
        this.checkedList = this.checkedList.filter(
          (checkItem) => checkItem !== +id
        );
      }

      this.indeterminate =
        !!this.checkedList.length &&
        this.checkedList.length < this.plainOptions.length;
      this.checkAll = this.checkedList.length === this.plainOptions.length;
    },

    onCheckAllChange(e) {
      console.log(e.target);
      const { checked } = e.target;

      const eachInput = document.querySelectorAll(".listItems");
      eachInput.forEach((item) =>
        checked
          ? item.childNodes[0].classList.add("ant-checkbox-checked")
          : item.childNodes[0].classList.remove("ant-checkbox-checked")
      );

      Object.assign(this, {
        checkedList: e.target.checked ? this.plainOptions : [],
        indeterminate: false,
        checkAll: checked,
      });
    },

    getCheckboxId() {
      const { data } = this.$props;
      const allDataId = data.map((item) => item.id);
      this.plainOptions = allDataId;
    },

    // TODO move to seller detail
    moveSellerDetails(e) {
      const { id } = e.target;
      this.$router.push(`/main/user/${id}`);
    },

    //  TODO search query
    searchInput(e) {
      const { value, id } = e.target;
      const searchInput = {
        [id]: value,
      };
      console.log(searchInput);
    },

    searchSellerStatus(value) {
      const searchInput = {
        seller_status: value,
      };
      console.log(searchInput);
    },

    searchSellerId(value) {
      const searchInput = { seller_attribute_id: value };
      console.log(searchInput);
    },

    onDateChange(date, dateString) {
      console.log(date, dateString);
    },

    confirmBtnColor(btn) {
      if (btn === "휴점 신청")
        return {
          background: `#f0ad4e`,
          border: "1px solid #eea236",
        };

      if (btn === "입점 승인")
        return {
          background: `#5bc0de`,
          border: "1px solid #46b8da",
        };

      if (btn === "퇴점신청 처리" || btn === "입점 거절")
        return {
          background: `#d9534f`,
          border: `1px solid #d43f3a`,
        };
    },
  },

  computed: {},

  // SECTION Life cycle
  beforeUpdate() {
    this.getCheckboxId();
  },
};
</script>

<style lang="scss" scoped>
@import "../../../styles/mixin.scss";

.sellers-content-main-table {
  margin: 0 10px;
  border: 1px solid #ddd;
  overflow-x: scroll;

  > table {
    min-width: 1350px;
    border-collapse: separate;
    /* margin-bottom: 5px; */
    > thead {
      height: 36px;
      background: #eee;
      font-weight: 700;
      > tr {
        > th {
          border-right: 1px solid #ddd;
          padding: 5px 5px;
          > div {
            width: 100%;
          }
          &:nth-child(1) {
            width: 40px;
            > div {
              @include flexSet("center", "center");
            }
          }
          &:nth-child(2) {
            width: 54px;
          }
          &:nth-child(3) {
            width: 118px;
          }
          &:nth-child(4) {
            width: 115px;
          }
          &:nth-child(5) {
            width: 99px;
          }
          &:nth-child(6) {
            width: 96px;
          }
          &:nth-child(7) {
            width: 65px;
          }
          &:nth-child(8) {
            width: 117px;
          }
          &:nth-child(9) {
            width: 105px;
          }
          &:nth-child(10) {
            width: 85px;
          }
          &:nth-child(11) {
            width: 159px;
          }
          &:nth-child(12) {
            width: 251px;
            border-right: 0;
          }
        }
      }
    }
    tbody {
      tr {
        height: 38px;
        &:nth-child(even) {
          background: #f5f5f5;
        }

        &:hover {
          background: darken($color: #f5f5f5, $amount: 2%);
        }

        &:first-child {
          &:hover {
            background: none;
          }

          td {
            padding: 10px;
            > div {
              @include flexSet(null, "flex-start", "column");

              > button {
                padding: 5px 10px;
                font-size: 12px;

                > span {
                  margin-left: 3px;
                }

                &:first-child {
                  background: #f0ad4e;
                  border-color: #eea236;
                  margin-bottom: 5px;

                  &:hover {
                    background: darken(#f0ad4e, 10%);
                  }
                }

                &:last-child {
                  background: #d9534f;
                  border-color: #d43f3a;

                  &:hover {
                    background: darken(#d9534f, 10%);
                  }
                }
              }
            }
          }
        }

        td {
          font-size: 13px;
          border-right: 1px solid #ddd;
          border-top: 1px solid #ddd;
          padding: 5px 10px;

          &:nth-child(3) {
            color: #0d638f;
            cursor: pointer;
            &:hover {
              text-decoration: underline;
            }
            div {
            }
          }
          &:nth-child(11) {
            > div {
              > span {
                &:last-child {
                  margin-top: 5px;
                }
              }
            }
          }
          &:last-child {
            border-right: 0;
            > span {
              button {
                padding: 3px;
                font-size: 12px;
                margin-right: 5px;
                line-height: 12px;
                height: 25px;
                color: #fff;
                &:last-child {
                  margin-right: 0;
                }
              }
            }
          }
        }
      }
    }
  }
}
</style>
