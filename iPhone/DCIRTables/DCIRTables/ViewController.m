//
//  ViewController.m
//  DCIRTables
//
//  Created by Alexei Gousev on 4/25/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController
@synthesize tables;
@synthesize tableView;
@synthesize navItem;

#define HEROKU_URL @"http://cold-galaxy-7337.herokuapp.com/get_api/"

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    self.tables = [NSMutableArray array];
    
    loading = false;
    [self updateTablesWrapper];
    
    // Add refresh button to Nav Bar
    UIBarButtonItem *anotherButton = [[UIBarButtonItem alloc] initWithTitle:@"Refresh" style:UIBarButtonItemStylePlain target:self action:@selector(updateTables)];
    self.navItem.rightBarButtonItem = anotherButton;

}

- (void)viewDidUnload
{
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    if ([[UIDevice currentDevice] userInterfaceIdiom] == UIUserInterfaceIdiomPhone) {
        return (interfaceOrientation != UIInterfaceOrientationPortraitUpsideDown);
    } else {
        return YES;
    }
}

// This function is to be called synchronously
-(void) updateTablesWrapper
{
    loading = true;
    [self performSelectorInBackground:@selector(updateTables) withObject:nil];
    
    // Reload the table view with the new data
    [self.tableView reloadData];
    
    // ToDo:  Display "loading..." text while this is happening.
}

// Asynchronously download the new tables
-(void) updateTables
{
    // Get tables string from URL
    NSError *err = nil;
    NSString *url = [[NSString stringWithFormat:HEROKU_URL] stringByAddingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
    NSString *tablesStr = [NSString stringWithContentsOfURL:[NSURL URLWithString:url] encoding:NSUTF8StringEncoding error:&err];
    
    // If URL load failed for some reason, display a nice popup alert saying so.
    if(err != nil) {
        UIAlertView *alertView = [[UIAlertView alloc] initWithTitle:@"Error!" message:@"Download failed." delegate:self cancelButtonTitle:@"OK" otherButtonTitles:nil];
        [alertView show];
        
        return;
    }
    
    loading = false;
    
    // Set the data
    self.tables = [NSMutableArray arrayWithArray:[tablesStr componentsSeparatedByString:@","]];
    
    // Reload the table view with the new data
    [self.tableView reloadData];
    
}

#pragma mark - Table view methods

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    return 1;
}

- (NSString *)tableView:(UITableView *)tableView titleForHeaderInSection:(NSInteger)section
{
    if(loading)
    {
        return @"Loading...";
    }
    
    else
    {
        return [NSString stringWithFormat:@"There are %d outstanding tables.", [tables count]];
    }
}

// Customize the number of rows in the table view.
- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return [self.tables count];
}

// Customize the appearance of table view cells.
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    
    static NSString *CellIdentifier = @"Cell";
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier];
    }
    
    // Configure the cell.
    cell.textLabel.text = [self.tables objectAtIndex: [indexPath row]];
    
    return cell;
}

@end
