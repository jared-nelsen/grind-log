import 'package:flutter/material.dart';

class LandingPage extends StatefulWidget {
  static String routeName = '/land';

  String _sessionId;

  LandingPage(this._sessionId);

  @override
  _LandingPageState createState() => _LandingPageState(this._sessionId);
}

class _LandingPageState extends State<LandingPage> {
  String _sessionID;

  _LandingPageState(this._sessionID);

  @override
  Widget build(BuildContext context) {
    return Scaffold();
  }
}
