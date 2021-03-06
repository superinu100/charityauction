import React, { PureComponent } from 'react'
import PropTypes from 'prop-types'
import { Field } from 'redux-form/immutable'


class FormField extends PureComponent {

  static propTypes = {
    children: PropTypes.node,
    component: PropTypes.func.isRequired,
    helpText: PropTypes.string,
    label: PropTypes.string,
    name: PropTypes.string.isRequired,
    options: PropTypes.any,
    getTitle: PropTypes.func,
    placeholder: PropTypes.string,
    type: PropTypes.string,
    validate: PropTypes.oneOfType([
      PropTypes.array,
      PropTypes.func
    ]),
    onChange: PropTypes.func,
  }

  render() {
    const {
      name, label, helpText, children, component, type, validate,
      options, getTitle, placeholder,
      onChange,
    } = this.props

    return (
      <Field name={name} component={component} type={type} validate={validate} onChange={onChange}
        props={{ children, label, helpText, options, getTitle, placeholder }} />
    )
  }
}

export default FormField
