/**
 * Author: Isamu Isozaki
 * Handles sign in
 */
import React from 'react';
import { connect } from 'react-redux';
import AuthScreen from 'app/screens/AuthScreen';
import Mood from 'app/screens/Mood';
import PropTypes from 'prop-types';

/**
 *
 * @param {object} param0
 */
function AuthNavigator({
  userIsInitializing
}) {
  if (!userIsInitializing) {
    return <Mood />
  } else {
    return <AuthScreen />
  }
}

AuthNavigator.propTypes = {
  token: PropTypes.string
}
const mapStateToProps = (state) => ({
  userIsInitializing: state.auth.isInitializing
});

export default connect(
  mapStateToProps,
  {},
)(AuthNavigator);
