/**
 * Author: Isamu Isozaki
 * Handles sign in
 */
import React from 'react';
import { connect } from 'react-redux';
import { loadMoods } from 'app/store/mood';
import AuthScreen from 'app/screens/AuthScreen';
import Mood from 'app/screens/Mood';
import PropTypes from 'prop-types';

/**
 *
 * @param {object} param0
 */
function AuthNavigator({
  userIsInitializing,
  moodIsInitializing,
  loadMoods
}) {
  console.log({moodIsInitializing})
  if (!userIsInitializing) {
    loadMoods()
  }
  if (!userIsInitializing && !moodIsInitializing) {
    return <Mood />
  } else {
    return <AuthScreen />
  }
}

AuthNavigator.propTypes = {
  userIsInitializing: PropTypes.bool,
  moodIsInitializing: PropTypes.bool,
  loadMoods: PropTypes.func
}
const mapStateToProps = (state) => ({
  userIsInitializing: state.auth.isInitializing,
  moodIsInitializing: state.mood.isInitializing
});

export default connect(
  mapStateToProps,
  {
    loadMoods
  },
)(AuthNavigator);
