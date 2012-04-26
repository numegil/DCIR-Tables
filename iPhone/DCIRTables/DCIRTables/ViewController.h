//
//  ViewController.h
//  DCIRTables
//
//  Created by Alexei Gousev on 4/25/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController <UITableViewDelegate, UITableViewDataSource>
{
    NSMutableArray *tables;
    IBOutlet UITableView *tableView;
    IBOutlet UINavigationItem *navItem;
    
    // Set to true if we are currently fetching data from the interwebz.
    bool loading;
}

-(void) updateTablesWrapper; // sync
-(void) updateTables; // async

@property(nonatomic, retain) NSMutableArray *tables;
@property(nonatomic, retain) IBOutlet UITableView *tableView;
@property(nonatomic, retain) IBOutlet UINavigationItem *navItem;

@end
