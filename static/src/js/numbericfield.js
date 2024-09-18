/** @odoo-module **/

import { registry } from "@web/core/registry";
import { _t } from "@web/core/l10n/translation";
import { useInputField } from "@web/views/fields/input_field_hook";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component } from "@odoo/owl";

export class NumbericField extends Component {
    static template = "health_employee.NumbericField";
    static props = {
        ...standardFieldProps,
        placeholder: { type: String, optional: true },
    };

    setup() {
        useInputField({ getValue: () => this.props.record.data[this.props.name] || "" });
    }
    validateAlphanumeric(event) {
        var charCode = event.charCode;
        if (!(/[0-9]/.test(String.fromCharCode(charCode)))) {
            event.preventDefault();
        }
    }
    get maxLength() {
        return this.props.record.fields[this.props.name].size;
    }
}

export const numbericField = {
    component: NumbericField,
    displayName: _t("Numberic"),
    supportedTypes: ["char"],
    extractProps: ({ attrs }) => ({
        placeholder: attrs.placeholder,
    }),
};

registry.category("fields").add("numberic_field", numbericField);
