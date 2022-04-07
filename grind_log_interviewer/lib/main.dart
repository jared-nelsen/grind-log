import 'package:flutter/material.dart';

import 'home_page.dart';
import 'landing_page.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Grind Log',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      initialRoute: HomePage.routeName,
      routes: {
        HomePage.routeName: (context) => HomePage(),
      },
      onGenerateRoute: (settings) {
        String? settingsName = settings.name;

        // We got an error with the settings name: Navigate back to Home
        if (settingsName == null) {
          return MaterialPageRoute(
            builder: (context) {
              return HomePage();
            },
          );
        }

        String specificRoute = settingsName.substring(0, 5);

        if (specificRoute == LandingPage.routeName) {
          Uri sessionURI = Uri.parse(settingsName);

          String? sessionID = sessionURI.queryParameters['id'];

          if (sessionID == null ||
              sessionID.isEmpty ||
              sessionID.length != 32) {
            //Maybe navigate to an error screen
            return MaterialPageRoute(
              builder: (context) {
                return HomePage();
              },
            );
          }

          return MaterialPageRoute(
            builder: (context) {
              return LandingPage(sessionID);
            },
          );
        }
      },
    );
  }
}
